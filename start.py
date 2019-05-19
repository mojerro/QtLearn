"""
    author: JoeyGaojingxing
    time:
"""
import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from UI.ui_main import Ui_MainWindow
from app import JosephusCircleWindow, NinePatchWindow
"""
TODO: beauty the GUI, such as backgrounds, layouts, window icon.
TODO: add global error handling, raise warnings when raise a error
"""

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
        self.josephus_circle = JosephusCircleWindow(self)
        self.NinePatchButton.clicked.connect(self.click_nine_patch)
        self.nine_patch = NinePatchWindow(self)

    @QtCore.Slot()
    def click_josephus_circle(self):
        self.josephus_circle.show()
        self.hide()

    @QtCore.Slot()
    def click_nine_patch(self):
        self.nine_patch.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # sys.exit(app.exec_())
    sys.exit(app.exec_())
