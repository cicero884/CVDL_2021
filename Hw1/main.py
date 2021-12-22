from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import prob1
import prob2
import prob3
import prob4

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui", self)
		
        #prob1
        self.btn1_1.clicked.connect(prob1.prob1_1)
        self.btn1_2.clicked.connect(prob1.prob1_2)
        self.btn1_3.clicked.connect(lambda: prob1.prob1_3(self.spinBox1_3.value()))
        self.btn1_4.clicked.connect(prob1.prob1_4)
        self.btn1_5.clicked.connect(prob1.prob1_5)
        
        self.btn2_1.clicked.connect(lambda: prob2.prob2(self.lineEdit2.text(),0))
        self.btn2_2.clicked.connect(lambda: prob2.prob2(self.lineEdit2.text(),1))

        self.btn3_1.clicked.connect(prob3.prob3_1)
        self.btn3_2.clicked.connect(prob3.prob3_2)

        self.btn4_1.clicked.connect(prob4.prob4_1)
        self.btn4_2.clicked.connect(prob4.prob4_2)
        self.btn4_3.clicked.connect(prob4.prob4_3)

if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())
