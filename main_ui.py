# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shouyezNgzOG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QMenuBar, QStatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 120, 131, 61))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 260, 131, 61))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 410, 131, 61))
        self.pushButton_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u8bba\u8bfe\u7a0b\u8bbe\u8ba1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u54c8\u592b\u66fc\u7f16\u7801", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8d39\u8bfa\u7f16\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u9999\u519c\u7f16\u7801", None))
    # retranslateUi

