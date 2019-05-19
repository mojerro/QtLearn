"""
    author: JoeyGaojingxing
    time:
"""
from app.JosephusCircle import josephus_circle_arr, josephus_circle_linked_list
import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from UI.ui_main import Ui_MainWindow
from app.JosephusCircle import JosephusCircleWindow

try:
    # Python v2.
    unicode


    def encode_utf8(ba):
        return unicode(ba, encoding='utf8')


    def decode_utf8(qs):
        return QtCore.QByteArray(str(qs))

except NameError:
    # Python v3.

    def encode_utf8(ba):
        return str(ba.data(), encoding='utf8')


    def decode_utf8(qs):
        return QtCore.QByteArray(bytes(qs, encoding='utf8'))


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.JosephusCircleButton.clicked.connect(self.click_josephus_circle)
        self.frame = JosephusCircleWindow(self)

    @QtCore.Slot()
    def click_josephus_circle(self):
        self.frame.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # sys.exit(app.exec_())
    app.exec_()
