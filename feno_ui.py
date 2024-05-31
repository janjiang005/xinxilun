# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanoVGeCvQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QStatusBar, QMenuBar, QLabel, QLineEdit, QTextEdit, QPushButton, QWidget



class Feno_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 770)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 180, 231, 251))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(180, 660, 181, 41))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 500, 181, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 560, 121, 41))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(180, 580, 181, 41))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(350, 180, 401, 251))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 130, 181, 51))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(350, 130, 181, 51))
        self.label_10.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 281, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 60, 121, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 141, 51))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 660, 141, 51))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_13.setFont(font2)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 490, 141, 51))
        self.label_11.setFont(font2)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 580, 141, 51))
        self.label_12.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d39\u8bfa\u7f16\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5404\u4fe1\u6e90\u7b26\u53f7\u6982\u7387", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7ed3\u679c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8d39\u8bfa\u7f16\u7801", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7b26\u53f7\u6570Q\uff08Q\u226510\uff09", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u6548\u7387\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u6e90\u71b5\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u7801\u957f\uff1a", None))
    # retranslateUi

