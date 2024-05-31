import sys
import main_ui       # coding就是通过.ui文件生成的.py文件，.ui文件的名字是什么就import什么
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
