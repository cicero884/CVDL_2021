from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import prob1


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui", self)
		
        #prob1
        self.btn1_1.clicked.connect(prob1.prob1_1)
        self.btn1_2.clicked.connect(prob1.prob1_2)
        self.btn1_3.clicked.connect(lambda: prob1.prob1_3(self.spinBox1_3.value()))
        


if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())

