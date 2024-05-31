import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from huffman import Mywindow as window1
from feno import Mywindow as window2
from shannon import Mywindow as window3

class Mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.huffman)#哈夫曼界面跳转
        self.ui.pushButton_2.clicked.connect(self.feno)#费诺界面跳转
        self.ui.pushButton_3.clicked.connect(self.shannon)#香农界面跳转

    def huffman(self):
        self.ui_huffman = window1()
        self.ui_huffman.show()
        self.close()

    def feno(self):
        self.ui_feno = window2()
        self.ui_feno.show()
        self.close()

    def shannon(self):
        self.ui_shannon = window3()
        self.ui_shannon.show()
        self.close()


    def back(self):
        self.ui_back = Mywindow()
        self.ui_back.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec_())