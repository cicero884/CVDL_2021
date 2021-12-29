from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import prob4
import prob5

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui", self)
		
        #prob4
        self.btn4_1.clicked.connect(prob4.prob4_1)
        self.btn4_2.clicked.connect(prob4.prob4_2)

        #prob5
        self.btn5_1.clicked.connect(prob5.prob5_1)
        self.btn5_2.clicked.connect(prob5.prob5_2)
        self.btn5_3.clicked.connect(prob5.prob5_3)
        self.btn5_4.clicked.connect(prob5.prob5_4)
if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())
