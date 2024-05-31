import math
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from feno_ui import Feno_MainWindow
class Node:
    def __init__(self, probability, position):
        self.P = probability  # 节点的概率或权重
        self.pos = position    # 节点的位置或索引

class Mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Feno_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Feno_Coding)


    def Feno_Coding(self):
        Q, sp = self.Read_Input()

        if Q == 0 and sp == 0:
            QMessageBox.warning(self, "Error", "Invalid input. Please check your input.")
            return
        sp_node = []
        print(Q)
        self.feno_code = [''] * len(sp)
        sp.sort(reverse=True)

        for i in range(len(sp)):
            sp_node.append(Node(sp[i], i))
        self.Coding(sp_node)
        # print(self.feno_code)
        outcome = ''
        for i in range(len(sp)):
            outcome = outcome + str(sp[i]) + '    ' + self.feno_code[i] + '    ' + '\n'
        self.ui.textEdit_2.setPlainText(outcome)
        self.Calculate_Performance_Index(sp, self.feno_code)


    def Coding(self, sp_node):
        if len(sp_node) == 1:
            return
        findPos = 0
        diff_c = 1
        sum1 = 0
        sum2 = 0
        left_flag = 0  # 0 means left bigger than right

        for i in range(len(sp_node) - 1):
            for j in range(i + 1):
                sum1 += sp_node[j].P
            for k in range(i + 1, len(sp_node)):
                sum2 += sp_node[k].P
            if abs(sum1 - sum2) < diff_c:
                diff_c = abs(sum1 - sum2)
                if sum1 < sum2:
                    left_flag = 1
                else:
                    left_flag = 0
                findPos = i
            sum1 = 0
            sum2 = 0

        for i in range(len(sp_node)):
            if left_flag:
                if i <= findPos:
                    self.feno_code[sp_node[i].pos] += '1'
                else:
                    self.feno_code[sp_node[i].pos] += '0'
            else:
                if i <= findPos:
                    self.feno_code[sp_node[i].pos] += '0'
                else:
                    self.feno_code[sp_node[i].pos] += '1'

        left = []
        right = []
        for i in range(findPos + 1):
            left.append(sp_node[i])
        for i in range(findPos + 1, len(sp_node)):
            right.append(sp_node[i])

        self.Coding(left)
        self.Coding(right)


    def Read_Input(self):

        Q = int(self.ui.lineEdit.text())  # num of symbol

        text = self.ui.textEdit.toPlainText()
        sp = self.Get_Symbol_Probability(text)  # symbol probability
        if Q < 10 or len(sp) != Q or sum(sp) < 0.99999:
            print('!!')
            # self.ui_error.show()
            # print(sum(sp))
            return 0, 0, 0, 0
        else:
            # print(Q,N,R,sp)
            return Q, sp


    def Str_Find_HH(self, str):  # HH:huan hang '\n'
        n = len(str)
        pos = list()
        for i in range(n):
            if str[i] == '\n':
                pos.append(i)
        #pos.append(i)
        #print(pos)
        return pos


    def Get_Symbol_Probability(self, str):
        n = len(str)
        pos = self.Str_Find_HH(str)
        sp = list()
        n_pos = len(pos)
        #print(n_pos)
        for i in range(n_pos):
            if i == 0:
                sp.append(float(str[0:pos[i]]))
            else:
                sp.append(float(str[pos[i - 1] + 1:pos[i]]))
        print(sp)
        return sp


    def Calculate_Performance_Index(self, sp, codes):
        HU = 0
        l_avr = 0
        for i in range(len(sp)):
            HU += -sp[i] * math.log2(sp[i])
        for i in range(len(sp)):
            l_avr += sp[i] * len(codes[i])
        effi = HU / l_avr / math.log2(2)
        print(effi)
        self.ui.lineEdit_2.setText(str(round(HU, 5)))
        self.ui.lineEdit_3.setText(str(round(l_avr, 2)))
        self.ui.lineEdit_4.setText(str(round(effi * 100, 4)) + '%')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec_())