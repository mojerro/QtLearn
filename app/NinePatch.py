import os
from ctypes import CDLL, c_char_p
from utils.utils import convert_byte
from UI.ui_nine_patch import Ui_NinePatchFrame
from PySide2.QtWidgets import QFrame, QTableWidgetItem
from PySide2.QtCore import SIGNAL, Slot

path = os.path.join(os.getcwd(), r'build\NinePatch.so')
# path = r'D:\Programming\QtLearn\build\NinePatch.so'
nine_patch_go = CDLL(path)


def nine_patch(edge: int) -> list:
    res = nine_patch_go.NinePatch
    res.restype = c_char_p
    return convert_byte(res(edge))[:edge**2]


class NinePatchWindow(QFrame, Ui_NinePatchFrame):

    def __init__(self, main):
        QFrame.__init__(self)
        self.setupUi(self)
        self.main = main
        self.edge = 3
        self.spinBoxEdge.setValue(self.edge)
        self.connect(self.spinBoxEdge, SIGNAL("valueChanged(int)"), self.set_edge)
        self.connect(self.pushButtonCommit, SIGNAL("clicked()"), self.run)

    def closeEvent(self, event=None):
        self.main.show()

    @Slot(int)
    def set_edge(self, val):
        self.edge = val

    @Slot()
    def run(self):
        self.tableWidgetResult.setColumnCount(self.edge)
        self.tableWidgetResult.setRowCount(self.edge)
        res = nine_patch(self.edge)
        num = 0
        for i in range(self.edge):
            for j in range(self.edge):
                self.tableWidgetResult.setItem(i, j, QTableWidgetItem(str(res[num])))
                num += 1
