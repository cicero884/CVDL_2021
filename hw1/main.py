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
        #self.btn4_1.clicked.connect(self.job4_1)



if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())

#
##prob1
#prob1_group=QGroupBox("1.Camera Calibration", window)
#layout.addWidget(prob1_group)
#prob1_layout=QVBoxLayout()
#prob1_group.setLayout(prob1_layout)
#
#prob1_layout.addWidget(QPushButton('Corner detection'))
#prob1_1_btn=QPushButton('intrinsic matrix')
#prob1_1_btn.clicked.connect(prob1_1)
#prob1_layout.addWidget(prob1_1_btn)
#prob1_layout.addWidget(QPushButton('extrinsic matrix'))
#prob1_layout.addWidget(QPushButton('distortion matrix'))
#prob1_layout.addWidget(QPushButton('undistorted result'))
#
##prob2
#
#window.setLayout(layout)
#window.show()
#app.exec()
