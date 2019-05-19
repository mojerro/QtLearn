# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/nine_patch.ui',
# licensing of './UI/nine_patch.ui' applies.
#
# Created: Sun May 19 23:04:06 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NinePatchFrame(object):
    def setupUi(self, NinePatchFrame):
        NinePatchFrame.setObjectName("NinePatchFrame")
        NinePatchFrame.resize(252, 290)
        self.verticalLayout = QtWidgets.QVBoxLayout(NinePatchFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelEdge = QtWidgets.QLabel(NinePatchFrame)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(16)
        self.labelEdge.setFont(font)
        self.labelEdge.setObjectName("labelEdge")
        self.horizontalLayout.addWidget(self.labelEdge)
        self.spinBoxEdge = QtWidgets.QSpinBox(NinePatchFrame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.spinBoxEdge.setFont(font)
        self.spinBoxEdge.setObjectName("spinBoxEdge")
        self.horizontalLayout.addWidget(self.spinBoxEdge)
        self.pushButtonCommit = QtWidgets.QPushButton(NinePatchFrame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.pushButtonCommit.setFont(font)
        self.pushButtonCommit.setObjectName("pushButtonCommit")
        self.horizontalLayout.addWidget(self.pushButtonCommit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetResult = QtWidgets.QTableWidget(NinePatchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetResult.sizePolicy().hasHeightForWidth())
        self.tableWidgetResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.tableWidgetResult.setFont(font)
        self.tableWidgetResult.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetResult.setIconSize(QtCore.QSize(5, 5))
        self.tableWidgetResult.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidgetResult.setObjectName("tableWidgetResult")
        self.tableWidgetResult.setColumnCount(0)
        self.tableWidgetResult.setRowCount(0)
        self.tableWidgetResult.horizontalHeader().setVisible(False)
        self.tableWidgetResult.horizontalHeader().setDefaultSectionSize(10)
        self.tableWidgetResult.horizontalHeader().setHighlightSections(False)
        self.tableWidgetResult.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidgetResult.verticalHeader().setVisible(False)
        self.tableWidgetResult.verticalHeader().setDefaultSectionSize(10)
        self.tableWidgetResult.verticalHeader().setHighlightSections(False)
        self.tableWidgetResult.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout.addWidget(self.tableWidgetResult)
        self.labelEdge.setBuddy(self.spinBoxEdge)

        self.retranslateUi(NinePatchFrame)
        QtCore.QMetaObject.connectSlotsByName(NinePatchFrame)
        NinePatchFrame.setTabOrder(self.spinBoxEdge, self.pushButtonCommit)
        NinePatchFrame.setTabOrder(self.pushButtonCommit, self.tableWidgetResult)

    def retranslateUi(self, NinePatchFrame):
        NinePatchFrame.setWindowTitle(QtWidgets.QApplication.translate("NinePatchFrame", "九宫图", None, -1))
        self.labelEdge.setText(QtWidgets.QApplication.translate("NinePatchFrame", "边长", None, -1))
        self.pushButtonCommit.setText(QtWidgets.QApplication.translate("NinePatchFrame", "提交", None, -1))
        self.pushButtonCommit.setShortcut(QtWidgets.QApplication.translate("NinePatchFrame", "Return", None, -1))
        self.tableWidgetResult.setSortingEnabled(False)

