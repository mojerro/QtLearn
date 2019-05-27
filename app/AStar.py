import os
from ctypes import CDLL, c_char_p
from utils.utils import convert_byte
from UI.ui_a_star import Ui_AStar
from PySide2.QtWidgets import QFrame, QTableWidgetItem
from PySide2.QtCore import SIGNAL, Slot

path = os.path.join(os.getcwd(), r'build\AStar.so')
# path = r'D:\Programming\QtLearn\build\NinePatch.so'
AStar = CDLL(path)


def a_star_b(size: bytes, init: bytes, goal: bytes, obstacles: bytes) -> bytes:
    res = AStar.AStarC
    res.restype = c_char_p
    res1 = res(size, init, goal, obstacles, len(obstacles))
    return res1


def a_star(size: list, init: list, goal: list, obstacles: list) -> list:
    size = list_to_bytes(size)
    init = list_to_bytes(init)
    goal = list_to_bytes(goal)
    obstacles = list_to_bytes(obstacles)
    res = a_star_b(size, init, goal, obstacles)
    return bytes_to_list(res)


def bytes_to_list(val: bytes) -> list:
    # TODO: bytes to 2D list
    pass


def list_to_bytes(val: list) -> bytes:
    # TODO: change n-D list to 1-D list then change to bytes
    pass


class AStarWindow(QFrame, Ui_AStar):

    def __init__(self, main):
        QFrame.__init__(self)
        self.setupUi(self)
        self.main = main
        self.table_size: list = [3, 4]
        self.spinBox_row.setValue(self.table_size[0])
        self.spinBox_col.setValue(self.table_size[1])
        self.start = [0, 0]
        self.end = [2, 2]
        self.obstacles = []  # 2D list like [[1, 2], [3, 4]] to show obstacles
        self.radio = ""  # TODO: record the radio button choose
        self.connect(self.spinBox_col, SIGNAL("valueChanged(int)"), self.set_col)
        self.connect(self.spinBox_row, SIGNAL("valueChanged(int)"), self.set_row)
        self.connect(self.pushButtonGenerate, SIGNAL("clicked()"), self.generate_table)
        self.connect(self.pushButtonResult, SIGNAL("clicked()"), self.run)
        # TODO: edit cell

    @Slot()
    def run(self):
        res = a_star(self.table_size, self.start, self.end, self.obstacles)
        # TODO:show res on table

    @Slot()
    def generate_table(self):
        self.tableWidget.setColumnCount(self.table_size[1])
        self.tableWidget.setRowCount(self.table_size[0])
        # TODO: add cell editable

    @Slot(int)
    def set_row(self, val: int):
        self.table_size[0] = val

    @Slot(int)
    def set_col(self, val: int):
        self.table_size[1] = val

    def closeEvent(self, event=None):
        self.main.show()


if __name__ == '__main__':
    print('res: res', convert_byte(a_star(b'\x05\x05', b'\x00\x00', b'\x04\x04', b'\x01\x02\x03\x04')))

# class NinePatchWindow(QFrame, Ui_NinePatchFrame):
#
#     def __init__(self, main):
#         QFrame.__init__(self)
#         self.setupUi(self)
#         self.main = main
#         self.edge = 3
#         self.spinBoxEdge.setValue(self.edge)
#         self.connect(self.spinBoxEdge, SIGNAL("valueChanged(int)"), self.set_edge)
#         self.connect(self.pushButtonCommit, SIGNAL("clicked()"), self.run)
#
#     def closeEvent(self, event=None):
#         self.main.show()
#
#     @Slot(int)
#     def set_edge(self, val):
#         self.edge = val
#
#     @Slot()
#     def run(self):
#         self.tableWidgetResult.setColumnCount(self.edge)
#         self.tableWidgetResult.setRowCount(self.edge)
#         res = nine_patch(self.edge)
#         num = 0
#         for i in range(self.edge):
#             for j in range(self.edge):
#                 self.tableWidgetResult.setItem(i, j, QTableWidgetItem(str(res[num])))
#                 num += 1
