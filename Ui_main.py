# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Martin_Code\Python\信息论\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lhy2020210593(object):
    def setupUi(self, lhy2020210593):
        lhy2020210593.setObjectName("lhy2020210593")
        lhy2020210593.resize(828, 600)
        self.lhy2020210593_2 = QtWidgets.QWidget(lhy2020210593)
        self.lhy2020210593_2.setObjectName("lhy2020210593_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.lhy2020210593_2)
        self.pushButton_1.setGeometry(QtCore.QRect(660, 10, 101, 41))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.lhy2020210593_2)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 70, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.lhy2020210593_2)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 130, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.lhy2020210593_2)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 190, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.lhy2020210593_2)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 250, 101, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_1 = QtWidgets.QTextEdit(self.lhy2020210593_2)
        self.textEdit_1.setGeometry(QtCore.QRect(20, 40, 531, 71))
        self.textEdit_1.setObjectName("textEdit_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.lhy2020210593_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 20, 113, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.lhy2020210593_2)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 150, 531, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.lhy2020210593_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.lhy2020210593_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 240, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.lhy2020210593_2)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 260, 531, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.lhy2020210593_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 350, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.lhy2020210593_2)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 370, 531, 71))
        self.textEdit_4.setObjectName("textEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.lhy2020210593_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 460, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.lhy2020210593_2)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 480, 531, 71))
        self.textEdit_5.setObjectName("textEdit_5")
        lhy2020210593.setCentralWidget(self.lhy2020210593_2)
        self.menuBar = QtWidgets.QMenuBar(lhy2020210593)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 828, 23))
        self.menuBar.setObjectName("menuBar")
        self.Fano = QtWidgets.QMenu(self.menuBar)
        self.Fano.setObjectName("Fano")
        self.Run = QtWidgets.QMenu(self.menuBar)
        self.Run.setObjectName("Run")
        self.singal = QtWidgets.QMenu(self.menuBar)
        self.singal.setObjectName("singal")
        self.Huffman = QtWidgets.QMenu(self.menuBar)
        self.Huffman.setObjectName("Huffman")
        self.Huff_Run = QtWidgets.QMenu(self.menuBar)
        self.Huff_Run.setObjectName("Huff_Run")
        lhy2020210593.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(lhy2020210593)
        self.statusbar.setObjectName("statusbar")
        lhy2020210593.setStatusBar(self.statusbar)
        self.menuBar.addAction(self.Huffman.menuAction())
        self.menuBar.addAction(self.Fano.menuAction())
        self.menuBar.addAction(self.Run.menuAction())
        self.menuBar.addAction(self.singal.menuAction())
        self.menuBar.addAction(self.Huff_Run.menuAction())

        self.retranslateUi(lhy2020210593)
        QtCore.QMetaObject.connectSlotsByName(lhy2020210593)

    def retranslateUi(self, lhy2020210593):
        _translate = QtCore.QCoreApplication.translate
        lhy2020210593.setWindowTitle(_translate("lhy2020210593", "MainWindow"))
        self.pushButton_1.setText(_translate("lhy2020210593", "Huffman"))
        self.pushButton_2.setText(_translate("lhy2020210593", "Fano"))
        self.pushButton_3.setText(_translate("lhy2020210593", "游程"))
        self.pushButton_4.setText(_translate("lhy2020210593", "算数"))
        self.pushButton_5.setText(_translate("lhy2020210593", "Huffman+Fano"))
        self.lineEdit_1.setText(_translate("lhy2020210593", "请输入被编码的字符串"))
        self.lineEdit_2.setText(_translate("lhy2020210593", "字符及其对应的编码"))
        self.lineEdit_3.setText(_translate("lhy2020210593", "编码结果"))
        self.lineEdit_4.setText(_translate("lhy2020210593", "译码结果"))
        self.lineEdit_5.setText(_translate("lhy2020210593", "编码效率"))
        self.Fano.setTitle(_translate("lhy2020210593", "Fano编码"))
        self.Run.setTitle(_translate("lhy2020210593", "游程编码"))
        self.singal.setTitle(_translate("lhy2020210593", "算数编码"))
        self.Huffman.setTitle(_translate("lhy2020210593", "Huffman编码"))
        self.Huff_Run.setTitle(_translate("lhy2020210593", "哈夫曼+游程"))
