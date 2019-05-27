# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/a_star.ui',
# licensing of './UI/a_star.ui' applies.
#
# Created: Mon May 27 11:38:24 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AStar(object):
    def setupUi(self, AStar):
        AStar.setObjectName("AStar")
        AStar.setWindowModality(QtCore.Qt.NonModal)
        AStar.setEnabled(True)
        AStar.resize(728, 626)
        self.verticalLayout = QtWidgets.QVBoxLayout(AStar)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_row = QtWidgets.QLabel(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label_row.setFont(font)
        self.label_row.setObjectName("label_row")
        self.horizontalLayout.addWidget(self.label_row)
        self.spinBox_row = QtWidgets.QSpinBox(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.spinBox_row.setFont(font)
        self.spinBox_row.setObjectName("spinBox_row")
        self.horizontalLayout.addWidget(self.spinBox_row)
        self.label_col = QtWidgets.QLabel(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label_col.setFont(font)
        self.label_col.setObjectName("label_col")
        self.horizontalLayout.addWidget(self.label_col)
        self.spinBox_col = QtWidgets.QSpinBox(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.spinBox_col.setFont(font)
        self.spinBox_col.setObjectName("spinBox_col")
        self.horizontalLayout.addWidget(self.spinBox_col)
        self.pushButtonGenerate = QtWidgets.QPushButton(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.pushButtonGenerate.setFont(font)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.horizontalLayout.addWidget(self.pushButtonGenerate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonResult = QtWidgets.QPushButton(AStar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.pushButtonResult.setFont(font)
        self.pushButtonResult.setObjectName("pushButtonResult")
        self.horizontalLayout.addWidget(self.pushButtonResult)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(AStar)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(AStar)
        QtCore.QMetaObject.connectSlotsByName(AStar)

    def retranslateUi(self, AStar):
        AStar.setWindowTitle(QtWidgets.QApplication.translate("AStar", "A*迷宫算法", None, -1))
        self.label_row.setText(QtWidgets.QApplication.translate("AStar", "行数", None, -1))
        self.label_col.setText(QtWidgets.QApplication.translate("AStar", "列数", None, -1))
        self.pushButtonGenerate.setText(QtWidgets.QApplication.translate("AStar", "生成迷宫", None, -1))
        self.pushButtonResult.setText(QtWidgets.QApplication.translate("AStar", "寻找通路", None, -1))

