from ctypes import CDLL, c_char_p
from utils.utils import convert_byte
from UI.ui_josephus_circle import Ui_JosephusCircleFrame
from PySide2.QtWidgets import QFrame, QApplication
from PySide2.QtCore import SIGNAL, Slot
import os, sys

"""
types:
9 5 1
[1 2 3 4 5 6 7 8 9]
end1 [5 1 7 4 3 6 9 2 8]
end2 [5 1 7 4 3 6 9 2 8]
result: 
b'\x05\x01\x07\x04\x03\x06\t\x02\x08\x01\x10\xac\xef\x01'
b'\x05\x01\x07\x04\x03\x06\t\x02\x08\x01\x10\xac\xef\x01'
"""

# path = os.path.join(os.getcwd(), r'build\JosephusCircle.so')
path = r'D:\Programming\QtLearn\build\JosephusCircle.so'
josephus = CDLL(path)


def josephus_circle_arr(length: int, times: int, starter: int) -> list:
    res = josephus.JosephusCircleArr
    res.restype = c_char_p
    return convert_byte(res(length, times, starter))[:length]


def josephus_circle_linked_list(length: int, times: int, starter: int) -> list:
    res = josephus.JosephusCircleLinkedList
    res.restype = c_char_p
    return convert_byte(res(length, times, starter))[:length]


class JosephusCircleWindow(QFrame, Ui_JosephusCircleFrame):

    def __init__(self, main):
        QFrame.__init__(self)
        self.setupUi(self)
        self.main = main
        self.people = 99
        self.starter = 1
        self.times = 5
        self.spinBox_times.setValue(self.times)
        self.spinBox_starter.setValue(self.starter)
        self.spinBox_people.setValue(self.people)
        self.connect(self.spinBox_people, SIGNAL("valueChanged(int)"), self.set_people)
        self.connect(self.spinBox_starter, SIGNAL("valueChanged(int)"), self.set_starter)
        self.connect(self.spinBox_times, SIGNAL("valueChanged(int)"), self.set_times)
        self.connect(self.commitButton, SIGNAL("clicked()"), self.run)

    @Slot(int)
    def set_people(self, val):
        self.people = val

    @Slot(int)
    def set_starter(self, val):
        self.starter = val

    @Slot(int)
    def set_times(self, val):
        self.times = val

    @Slot()
    def run(self):
        print(self.people, self.times, self.starter, self.comboBox.currentText())
        if self.comboBox.currentText() == "数组":
            res = josephus_circle_arr(self.people, self.times, self.starter)
        elif self.comboBox.currentText() == "链表":
            res = josephus_circle_linked_list(self.people, self.times, self.starter)
        else:
            raise NameError
        print('res', res)
        self.labelResult.setText(str(res))

    def closeEvent(self, event=None):
        if event is not None:
            self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JosephusCircleWindow()
    window.show()
    # sys.exit(app.exec_())
    app.exec_()
