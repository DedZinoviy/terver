# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\demon\Desktop\TerVer\myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.formula_img = QtWidgets.QLabel(self.centralwidget)
        self.formula_img.setText("")
        self.formula_img.setScaledContents(False)
        self.formula_img.setAlignment(QtCore.Qt.AlignCenter)
        self.formula_img.setObjectName("formula_img")
        self.verticalLayout.addWidget(self.formula_img)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.m_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.m_label.setFont(font)
        self.m_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.m_label.setObjectName("m_label")
        self.horizontalLayout.addWidget(self.m_label)
        self.m_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m_spinBox.setFont(font)
        self.m_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.m_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.m_spinBox.setMinimum(1)
        self.m_spinBox.setMaximum(1000)
        self.m_spinBox.setObjectName("m_spinBox")
        self.horizontalLayout.addWidget(self.m_spinBox)
        self.n_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_label.setFont(font)
        self.n_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.n_label.setObjectName("n_label")
        self.horizontalLayout.addWidget(self.n_label)
        self.n_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_spinBox.setFont(font)
        self.n_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.n_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.n_spinBox.setMinimum(1)
        self.n_spinBox.setMaximum(1000)
        self.n_spinBox.setObjectName("n_spinBox")
        self.horizontalLayout.addWidget(self.n_spinBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.result_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_textEdit.setFont(font)
        self.result_textEdit.setReadOnly(True)
        self.result_textEdit.setObjectName("result_textEdit")
        self.verticalLayout.addWidget(self.result_textEdit)
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solve_button.setFont(font)
        self.solve_button.setObjectName("solve_button")
        self.verticalLayout.addWidget(self.solve_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Сочетания"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Сочетания с повторениями"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Размещения с повторением"))
        self.m_label.setText(_translate("MainWindow", "m = "))
        self.n_label.setText(_translate("MainWindow", "n = "))
        self.label_2.setText(_translate("MainWindow", "n,m∈(0;1000]"))
        self.solve_button.setText(_translate("MainWindow", "Решить"))
