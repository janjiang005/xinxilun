import math
import sys


from PyQt5 import QtWidgets
from huffman_ui import Huffman_MainWindow



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'huffmanSlIkBp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Node:
    def __init__(self, probability, position):
        self.P = probability  # 节点的概率或权重
        self.pos = position    # 节点的位置或索引


class Node_2:
    def __init__(self, probability):
        self.child1 = None
        self.child2 = None
        self.father = None
        self.P = probability
    def check_num_of_child(self):
        return self.father.child1 == self

class Node_3:
    def __init__(self, probability):
        self.P = probability
        self.father = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
    def check_num_of_child(self):
        if self.father.child1 == self:
            return 0
        elif self.father.child2 == self:
            return 1
        else:
            return 2

class Node_4:
    def __init__(self, probability):
        self.P = probability
        self.father = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None

    def check_num_of_child(self):
        if self.father.child1 == self:
            return 0
        elif self.father.child2 == self:
            return 1
        elif self.father.child3 == self:
            return 2
        else:
            return 3

class Node_5:
    def __init__(self, probability):
        self.P = probability
        self.father = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.child5 = None

    def check_num_of_child(self):
        if self.father.child1 == self:
            return 0
        elif self.father.child2 == self:
            return 1
        elif self.father.child3 == self:
            return 2
        elif self.father.child4 == self:
            return 3
        else:
            return 4

class Mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Huffman_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Hoffman_Coding)



    def Hoffman_Coding(self):

        Q,N,R,sp = self.Read_Input()
        if Q == 0 and N == 0 and R == 0 and sp == 0:
            self.ui_error.show()
            return 0
        all_sym = self.Get_All_Symbol(Q,N,R,sp)      # all nodes
        if R == 2:
            hoffman_tree = self.Hoffman_Tree_Generate_2(Q,N,sp,all_sym)
            hoffman_code = self.Coding_2(all_sym,hoffman_tree)
            outcome = ''
            for i in range(len(all_sym)):
                outcome = outcome + str(round(all_sym[i].P,6)) + '    ' + hoffman_code[i] + '    ' +'\n'
            # print(outcome)
            self.ui.textEdit_2.setPlainText(outcome)
            self.Calculate_Performance_Index(N,R,sp,all_sym,hoffman_code)
        elif R == 3:
            hoffman_tree = self.Hoffman_Tree_Generate_3(Q,N,sp,all_sym)
            hoffman_code = self.Coding_3(all_sym, hoffman_tree)
            outcome = ''
            for i in range(len(all_sym)):
                outcome = outcome + str(round(all_sym[i].P, 6)) + '    ' + hoffman_code[i] + '    ' + '\n'
            self.ui.textEdit_2.setPlainText(outcome)
            self.Calculate_Performance_Index(N, R, sp, all_sym, hoffman_code)
        elif R == 4:
            hoffman_tree = self.Hoffman_Tree_Generate_4(Q,N,sp,all_sym)
            hoffman_code = self.Coding_4(all_sym, hoffman_tree)
            outcome = ''
            for i in range(len(all_sym)):
                outcome = outcome + str(round(all_sym[i].P, 6)) + '    ' + hoffman_code[i] + '    ' + '\n'
            self.ui.textEdit_2.setPlainText(outcome)
            self.Calculate_Performance_Index(N, R, sp, all_sym, hoffman_code)
        elif R == 5:
            hoffman_tree = self.Hoffman_Tree_Generate_5(Q,N,sp,all_sym)
            hoffman_code = self.Coding_5(all_sym, hoffman_tree)
            outcome = ''
            for i in range(len(all_sym)):
                outcome = outcome + str(round(all_sym[i].P, 6)) + '    ' + hoffman_code[i] + '    ' + '\n'
            self.ui.textEdit_2.setPlainText(outcome)
            self.Calculate_Performance_Index(N, R, sp, all_sym, hoffman_code)


    def Hoffman_Tree_Generate_2(self,Q,N,sp,all_sym):
        queue = all_sym[:]
        while len(queue) > 1:
            queue.sort(key=lambda item:item.P)
            node_child1 = queue.pop(0)
            node_child2 = queue.pop(0)
            node_father = Node_2(node_child1.P + node_child2.P)
            node_father.child1 = node_child1
            node_father.child2 = node_child2
            node_child1.father = node_father
            node_child2.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]

    def Hoffman_Tree_Generate_3(self,Q,N,sp,all_sym):
        queue = all_sym[:]
        while len(queue) > 1:
            queue.sort(key=lambda item:item.P)
            node_child1 = queue.pop(0)
            node_child2 = queue.pop(0)
            node_child3 = queue.pop(0)
            node_father = Node_3(node_child1.P + node_child2.P + node_child3.P)
            node_father.child1 = node_child1
            node_father.child2 = node_child2
            node_father.child3 = node_child3
            node_child1.father = node_father
            node_child2.father = node_father
            node_child3.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]

    def Hoffman_Tree_Generate_4(self,Q,N,sp,all_sym):
        queue = all_sym[:]
        while len(queue) > 1:
            queue.sort(key=lambda item:item.P)
            node_child1 = queue.pop(0)
            node_child2 = queue.pop(0)
            node_child3 = queue.pop(0)
            node_child4 = queue.pop(0)
            node_father = Node_4(node_child1.P + node_child2.P + node_child3.P + node_child4.P)
            node_father.child1 = node_child1
            node_father.child2 = node_child2
            node_father.child3 = node_child3
            node_father.child4 = node_child4
            node_child1.father = node_father
            node_child2.father = node_father
            node_child3.father = node_father
            node_child4.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]

    def Hoffman_Tree_Generate_5(self,Q,N,sp,all_sym):
        queue = all_sym[:]
        while len(queue) > 1:
            queue.sort(key=lambda item:item.P)
            node_child1 = queue.pop(0)
            node_child2 = queue.pop(0)
            node_child3 = queue.pop(0)
            node_child4 = queue.pop(0)
            node_child5 = queue.pop(0)
            node_father = Node_5(node_child1.P + node_child2.P + node_child3.P + node_child4.P + node_child5.P)
            node_father.child1 = node_child1
            node_father.child2 = node_child2
            node_father.child3 = node_child3
            node_father.child4 = node_child4
            node_father.child5 = node_child5
            node_child1.father = node_father
            node_child2.father = node_father
            node_child3.father = node_father
            node_child4.father = node_father
            node_child5.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]


    def Coding_2(self,all_sym,root):
        codes = ['']*len(all_sym)
        for i in range(len(all_sym)):
            node_tem = all_sym[i]
            while node_tem != root:
                if node_tem.check_num_of_child() == 1:
                    codes[i] = '0' + codes[i]
                else:
                    codes[i] = '1' + codes[i]
                node_tem = node_tem.father
        print(codes)
        return codes


    def Coding_3(self, all_sym, root):
        codes = ['']*len(all_sym)
        for i in range(len(all_sym)):
            node_tem = all_sym[i]
            while node_tem != root:
                if node_tem.check_num_of_child() == 1:
                    codes[i] = '0' + codes[i]
                elif node_tem.check_num_of_child() == 2:
                    codes[i] = '1' + codes[i]
                else:
                    codes[i] = '2' + codes[i]
                node_tem = node_tem.father
        print(codes)
        return codes

    def Coding_4(self, all_sym, root):
        codes = ['']*len(all_sym)
        for i in range(len(all_sym)):
            node_tem = all_sym[i]
            while node_tem != root:
                if node_tem.check_num_of_child() == 1:
                    codes[i] = '0' + codes[i]
                elif node_tem.check_num_of_child() == 2:
                    codes[i] = '1' + codes[i]
                elif node_tem.check_num_of_child() == 3:
                    codes[i] = '2' + codes[i]
                else:
                    codes[i] = '3' + codes[i]
                node_tem = node_tem.father
        print(codes)
        return codes

    def Coding_5(self, all_sym, root):
        codes = ['']*len(all_sym)
        for i in range(len(all_sym)):
            node_tem = all_sym[i]
            while node_tem != root:
                if node_tem.check_num_of_child() == 1:
                    codes[i] = '0' + codes[i]
                elif node_tem.check_num_of_child() == 2:
                    codes[i] = '1' + codes[i]
                elif node_tem.check_num_of_child() == 3:
                    codes[i] = '2' + codes[i]
                elif node_tem.check_num_of_child() == 4:
                    codes[i] = '3' + codes[i]
                else:
                    codes[i] = '4' + codes[i]
                node_tem = node_tem.father
        print(codes)
        return codes

    def Get_All_Symbol(self,Q,N,R,sp):
        all_sym = []
        symbol_sequence = []
        nodes = []
        for i in range(N):
            symbol_sequence.append(0)
        for i in range(pow(Q,N)):
            j = N-1
            P = sp[symbol_sequence[0]]
            for k in range(N):
                if k != 0:
                    P *= sp[symbol_sequence[k]]
            if R == 2:
                all_sym.append(Node_2(P))
            elif R == 3:
                all_sym.append(Node_3(P))
            elif R == 4:
                all_sym.append(Node_4(P))
            elif R == 5:
                all_sym.append(Node_5(P))

            while symbol_sequence[j] == Q-1:
                symbol_sequence[j] = 0
                j -= 1
                if j == -1:
                    # print(len(all_sym))
                    if( int((Q - R)/(R - 1))!=(Q - R)/(R - 1) ):
                        Q_expand = int((Q - R)/(R - 1)+1)*(R - 1)+R
                        for i in range(Q_expand - Q):
                            if R == 2:
                                all_sym.append(Node_2(0))
                            elif R == 3:
                                all_sym.append(Node_3(0))
                            elif R == 4:
                                all_sym.append(Node_4(0))
                            elif R == 5:
                                all_sym.append(Node_5(0))
                    return all_sym
            symbol_sequence[j] += 1

    def Read_Input(self):

        Q = int(self.ui.lineEdit_5.text()) # num of symbol
        N = int(self.ui.lineEdit_6.text())# num of sequence
        R = int(self.ui.lineEdit_7.text())  # num of radix


        text = self.ui.textEdit.toPlainText()

        sp = self.Get_Symbol_Probability(text)  # symbol probability

        if Q<8 or Q>15 or N<1 or N>3 or R<2 or R>5 or len(sp)!=Q or sum(sp) < 0.99999:
            print('!!')
            # self.ui_error.show()
            # print(sum(sp))
            return 0,0,0,0
        else:
            # print(Q,N,R,sp)
            return Q,N,R,sp

    def Str_Find_HH(self,str):  # HH:huan hang '\n'
        n = len(str)
        pos = list()
        for i in range(n):
            if str[i] == '\n':
                pos.append(i)
        # print(pos)
        return pos

    def Get_Symbol_Probability(self,str):
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


    def Calculate_Performance_Index(self,N,R,sp,all_sym,codes):
        HU = 0
        l_avr = 0
        for i in range(len(sp)):
            HU += -sp[i]*math.log2(sp[i])
        for i in range(len(all_sym)):
            l_avr += all_sym[i].P*len(codes[i])
        effi = HU*N/l_avr/math.log2(R)

        self.ui.lineEdit_2.setText(str(round(HU,5)))
        self.ui.lineEdit_3.setText(str(round(l_avr,2)))
        self.ui.lineEdit_4.setText(str(round(effi*100,4))+'%')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec_())