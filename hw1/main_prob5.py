from PyQt5 import QtCore, QtGui, QtWidgets, uic
import numpy
from matplotlib import pyplot
from matplotlib import image
import sys

import prob5_train

cifar_label=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','trunk']

def prob5_1():
    fig = pyplot.gcf()
    fig.set_size_inches(35, 35)
    for i in range(9):
        ax = pyplot.subplot(3,3,i+1)
        # ax.
        ax.imshow(prob5_train.x_train[i])
        ax.set_title(cifar_label[prob5_train.Y_train[i][0]])
    pyplot.show()

def prob5_2():
    print('batch size: ',prob5_train.Batch_size)
    print('learning rate: ',prob5_train.Learning_rate)
    print('optimizer: ',prob5_train.Optimizer.get_config())

def prob5_3():
    model=prob5_train.construct_vgg16()
    print(model.summary())

def prob5_4():
    accuracy = image.imread('accuracy.png')
    loss = image.imread('loss.png')
    pyplot.imshow(accuracy)
    pyplot.show()
    pyplot.imshow(loss)
    pyplot.show()

def prob5_5(index):
    index=int(index)
    model=prob5_train.load_trained_model()
    model.evaluate(prob5_train.x_test,prob5_train.y_test)
    
   #predict = model.predict(prob5_train.x_test[index].reshape(-1, 32, 32, 3))

   #testlebal = cifar_label[prob5_train.Y_test[index][0]]
   #pyplot.title(testlebal)
   #pyplot.imshow(prob5_train.x_test[index])
   #pyplot.show()

   #fig = pyplot.figure()
   #x = numpy.arange(len(cifar_label))
   #pyplot.bar(x, predict[0])
   #pyplot.xticks(x, cifar_label)
   #fig.set_figheight(6)
   #fig.set_figwidth(10)
   #pyplot.show()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        uic.loadUi("prob5.ui", self)
		
        #prob1
        self.btn5_1.clicked.connect(prob5_1)
        self.btn5_2.clicked.connect(prob5_2)
        self.btn5_3.clicked.connect(prob5_3)
        self.btn5_4.clicked.connect(prob5_4)
        self.btn5_5.clicked.connect(lambda: prob5_5(self.lineEdit_input.text()))
        self.btn5_6.clicked.connect(prob5_train.train)
        

if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())
