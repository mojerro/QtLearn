import os
from ctypes import CDLL, c_char_p
from utils.utils import convert_byte
from UI.ui_a_star import Ui_AStar
from PySide2.QtWidgets import QFrame, QTableWidgetItem
from PySide2.QtCore import SIGNAL, Slot

path = os.path.join(os.getcwd(), r'build\AStar.so')
# path = r'D:\Programming\QtLearn\build\NinePatch.so'
AStar = CDLL(path)


def a_star_b(size: bytes, init: bytes, goal: bytes, obstacles: bytes) -> list:
    res = AStar.AStarC
    res.restype = c_char_p
    res1 = res(size, init, goal, obstacles, len(obstacles))
    return convert_byte(res1, -1)


def a_star(size: list, init: list, goal: list, obstacles: list) -> list:
    size = list_to_bytes(size)
    init = list_to_bytes(init, 1)
    goal = list_to_bytes(goal, 1)
    obstacles = list_to_bytes(obstacles, 1)
    print(size, init, goal, obstacles, "a star test")
    res = a_star_b(size, init, goal, obstacles)
    # res = a_star_b(b'\x06\x06', b'\x01\x01', b'\x04\x04', b'\x03\x03')
    mid0, arr = [0, 0], []
    length = res.pop(0)
    print(length)
    res = res[:length * 2]
    for i in range(len(res)):
        if i % 2 == 0:
            mid = mid0.copy()
            mid[0] = res[i]
        else:
            mid[1] = res[i]
            arr.append(mid)
    return arr


def open_list(val: list, num: int = 0) -> list:
    # covert n-D list to 1-D list and plus 1
    res = []
    for j in val:
        if isinstance(j, list):
            li = open_list(j)
            for v in li:
                res.append(v + num)
        else:
            res.append(j + num)
    return res


def list_to_bytes(val: list, num: int = 0) -> bytes:
    # change n-D list to 1-D list then change to bytes
    arr = open_list(val, num)
    byte_arr = bytearray(arr)
    res = bytes(byte_arr)
    return res


class AStarWindow(QFrame, Ui_AStar):

    def __init__(self, main):
        QFrame.__init__(self)
        self.setupUi(self)
        self.main = main
        self.table_size: list = [6, 5]
        self.spinBox_row.setValue(self.table_size[0])
        self.spinBox_col.setValue(self.table_size[1])
        self.start = [1, 1]
        self.end = [5, 4]
        self.obstacles = [[1, 3]]  # 2D list like [[1, 2], [3, 4]] to show obstacles
        self.radio = ""
        self.connect(self.spinBox_col, SIGNAL("valueChanged(val)"), self.set_col)
        self.connect(self.spinBox_row, SIGNAL("valueChanged(int)"), self.set_row)
        self.connect(self.pushButtonGenerate, SIGNAL("clicked()"), self.generate_table)
        self.connect(self.pushButtonResult, SIGNAL("clicked()"), self.run)

        self.radioButtonInit.toggled.connect(lambda: self.radio_change(self.radioButtonInit))
        self.radioButtonGoal.toggled.connect(lambda: self.radio_change(self.radioButtonGoal))
        self.radioButtonObstacles.toggled.connect(lambda: self.radio_change(self.radioButtonObstacles))
        # TODO: edit cell
        self.connect(self.tableWidgetResult, SIGNAL("cellClicked(int, int)"), self.on_click_cell)
        self.generate_table()

    @Slot()
    def radio_change(self, val):
        self.radio = val.text()

    @Slot(int, int)
    def on_click_cell(self, row, col):
        try:
            val = self.tableWidgetResult.takeItem(row, col).text()
        except AttributeError:
            val = None
        if val is None:
            if self.radio == "牛郎":
                self.start[0] = row
                self.start[1] = col
            elif self.radio == "织女":
                self.end[0] = row
                self.end[1] = col
            elif self.radio == "墙":
                self.obstacles.append([row, col])
            self.tableWidgetResult.setItem(row, col, QTableWidgetItem(self.radio))
            self.generate_table()
        elif val == self.radio:
            if val == "牛郎":
                self.start = [-1, -1]
            elif val == "织女":
                self.end = [-1, -1]
            elif val == "墙":
                self.obstacles.remove([row, col])
            self.tableWidgetResult.setItem(row, col, None)
        else:
            if self.radio == "牛郎":
                self.start[0] = row
                self.start[1] = col
            elif self.radio == "织女":
                self.end[0] = row
                self.end[1] = col
            elif self.radio == "墙":
                self.obstacles.append([row, col])
            if val == "墙":
                self.obstacles.remove([row, col])
            self.tableWidgetResult.setItem(row, col, QTableWidgetItem(self.radio))
            self.generate_table()

    @Slot()
    def run(self):
        try:
            self.obstacles.remove([-1, -1])
        finally:
            self.obstacles.append([-1, -1])  # prevent None-value-error
            res = a_star(self.table_size, self.start, self.end, self.obstacles)
            # TODO:show res on table
            print('rqewr', res)
            for i in range(1, len(res)):
                # TODO：change the style of road
                self.tableWidgetResult.setItem(res[i][0] - 1, res[i][1] - 1, QTableWidgetItem("鹊桥"))

    @Slot()
    def generate_table(self):
        for row in range(self.table_size[0]):
            for col in range(self.table_size[1]):
                self.tableWidgetResult.setItem(row, col, None)
        self.tableWidgetResult.setColumnCount(self.table_size[1])
        self.tableWidgetResult.setRowCount(self.table_size[0])
        # TODO: init cell style change
        self.tableWidgetResult.setItem(self.start[0], self.start[1], QTableWidgetItem("牛郎"))
        # TODO: goal cell style change
        self.tableWidgetResult.setItem(self.end[0], self.end[1], QTableWidgetItem("织女"))
        # TODO: obstacles
        for arr in self.obstacles:
            self.tableWidgetResult.setItem(arr[0], arr[1], QTableWidgetItem("墙"))

    @Slot(int)
    def set_row(self, val: int):
        self.table_size[0] = val

    @Slot(int)
    def set_col(self, val: int):
        self.table_size[1] = val

    def closeEvent(self, event=None):
        self.main.show()


if __name__ == '__main__':
    print('res: res', convert_byte(a_star_b(b'\x05\x05', b'\x00\x00', b'\x04\x04', b'\x01\x02\x03\x04')))

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
