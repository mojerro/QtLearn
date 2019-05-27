# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/main.ui',
# licensing of './UI/main.ui' applies.
#
# Created: Mon May 27 11:56:53 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/favicon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NinePatchButton = QtWidgets.QPushButton(self.centralwidget)
        self.NinePatchButton.setGeometry(QtCore.QRect(300, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(16)
        self.NinePatchButton.setFont(font)
        self.NinePatchButton.setObjectName("NinePatchButton")
        self.JosephusCircleButton = QtWidgets.QPushButton(self.centralwidget)
        self.JosephusCircleButton.setGeometry(QtCore.QRect(100, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(16)
        self.JosephusCircleButton.setFont(font)
        self.JosephusCircleButton.setObjectName("JosephusCircleButton")
        self.AStarButton = QtWidgets.QPushButton(self.centralwidget)
        self.AStarButton.setGeometry(QtCore.QRect(100, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(16)
        self.AStarButton.setFont(font)
        self.AStarButton.setObjectName("AStarButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.JosephusCircleButton, self.NinePatchButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "41607497 高景行 数据结构 主页", None, -1))
        self.NinePatchButton.setText(QtWidgets.QApplication.translate("MainWindow", "Nine Patch", None, -1))
        self.JosephusCircleButton.setText(QtWidgets.QApplication.translate("MainWindow", "Josephus Circle", None, -1))
        self.AStarButton.setText(QtWidgets.QApplication.translate("MainWindow", "A Star Path Finding", None, -1))
        self.actionnew.setText(QtWidgets.QApplication.translate("MainWindow", "new", None, -1))
