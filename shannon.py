import math
import sys

from PyQt5 import QtWidgets

from shannon_ui import Shannon_MainWindow

class Mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Shannon_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Shannon_Coding)




    def Shannon_Coding(self):
        Q, sp = self.Read_Input()
        if Q == 0 and sp == 0:
            self.ui_error.show()
            return

        shannon_code = [''] * len(sp)
        sp.sort(reverse=True)
        for i in range(len(sp)):
            P_acc = 0
            code = ''
            l = int(-math.log2(sp[i]) + 1)
            for j in range(i):
                P_acc += sp[j]
            while True:
                P_acc *= 2
                if P_acc >= 1:
                    code += '1'
                else:
                    code += '0'
                if len(code) == l:
                    break
                P_acc -= int(P_acc)
                if P_acc == 0:
                    if (len(code) < l):
                        code += '0' * (l - len(code))
                        break
            shannon_code[i] = code[:l]
        # print(shannon_code)

        outcome = ''
        for i in range(len(sp)):
            outcome = outcome + str(sp[i]) + '    ' + shannon_code[i] + '    ' + '\n'
        self.ui.textEdit_2.setPlainText(outcome)
        self.Calculate_Performance_Index(sp, shannon_code)


    def Read_Input(self):
        Q = int(self.ui.lineEdit.text())  # num of symbol
        text = self.ui.textEdit.toPlainText()
        sp = self.Get_Symbol_Probability(text)  # symbol probability
        if Q < 10 or len(sp) != Q or sum(sp) < 0.99999:
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
        # print(pos)
        return pos


    def Get_Symbol_Probability(self, str):
        n = len(str)
        pos = self.Str_Find_HH(str)
        sp = list()
        n_pos = len(pos)
        for i in range(n_pos):
            if i == 0:
                sp.append(float(str[0:pos[i]]))
            else:
                sp.append(float(str[pos[i - 1] + 1:pos[i]]))
        # print(sp)
        return sp


    def Calculate_Performance_Index(self, sp, codes):
        HU = 0
        l_avr = 0
        for i in range(len(sp)):
            HU += -sp[i] * math.log2(sp[i])
        for i in range(len(sp)):
            l_avr += sp[i] * len(codes[i])
        effi = HU / l_avr / math.log2(2)

        self.ui.lineEdit_2.setText(str(round(HU, 5)))
        self.ui.lineEdit_3.setText(str(round(l_avr, 2)))
        self.ui.lineEdit_4.setText(str(round(effi * 100, 4)) + '%')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec_())