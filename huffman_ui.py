# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'huffmanVknHOi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5 import Qt
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QToolBar, QMenuBar, QLineEdit, QPushButton, QLabel, QTextEdit, QWidget


class Huffman_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 141, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 40, 141, 51))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(610, 40, 141, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 191, 51))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 120, 181, 51))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 170, 231, 251))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(360, 120, 181, 51))
        self.label_10.setFont(font1)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(360, 170, 401, 251))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 480, 111, 51))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_11.setFont(font2)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 570, 111, 51))
        self.label_12.setFont(font2)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 650, 101, 51))
        self.label_13.setFont(font2)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(180, 50, 121, 41))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(470, 50, 121, 41))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(760, 50, 121, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(520, 550, 121, 41))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 490, 181, 41))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 570, 181, 41))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(170, 650, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 23))
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u54c8\u592b\u66fc\u7f16\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7b26\u53f7\u6570Q\uff088\u2264Q\u226415\uff09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u5217\u6570N\uff081\u2264N\u22643\uff09", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5236\u6570R\uff082\u2264R\u22645\uff09", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u54c8\u592b\u66fc\u7f16\u7801", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5404\u4fe1\u6e90\u7b26\u53f7\u6982\u7387", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7ed3\u679c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u6e90\u71b5\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u7801\u957f\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u6548\u7387\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))

    # retranslateUi

