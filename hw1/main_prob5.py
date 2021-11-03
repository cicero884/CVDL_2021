from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

import prob5_train

cifar_label=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','trunk']

def prob5_1():
    fig = plt.gcf()
    fig.set_size_inches(35, 35)
    for i in range(9):
        ax = plt.subplot(3, 3, 1 + i)
        # ax.
        ax.imshow(x_train[i])
        ax.set_title(cifar_label[Y_train[i][0]])
    plt.show()

def prob5_2():
    print('Batch Size {}',format(Batch_size))
    model=prob5_train.load_model()
    parameter=model.get_config()
    print('\n{}',parameter)

def prob5_3():
    model=prob5_train.construct_vgg16()
    print(model.summary())

def prob5_4():
    accuracy = img.imread('accuracy.png')
    loss = img.imread('loss.png')
    plt.imshow(accuracy)
    plt.show()
    plt.imshow(loss)
    plt.show()

def prob5_5(index):
    model=prob5_train.load_model()
    predict = model.predict(x_test[n].reshape(-1, 32, 32, 3))

    testlebal = cifar_label[Y_test[n][0]]
    plt.title(testlebal)
    plt.imshow(x_test[n])
    plt.show()

    fig = plt.figure()
    x = np.arange(len(cifar_label))
    plt.bar(x, predict[0])
    plt.xticks(x, cifar_label)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.show()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui", self)
		
        #prob1
        self.btn5_1.clicked.connect(prob5_1)
        self.btn5_2.clicked.connect(prob5_2)
        self.btn5_3.clicked.connect(prob5_3)
        self.btn5_4.clicked.connect(prob5_4)
        self.btn5_5.clicked.connect(lambda: prob5.prob5_5(self.spinBox5_5.value()))
        self.btn5_6.clicked.connect(prob5_train.train())
        

if __name__ == "__main__": 
    Application = QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    mainwindow.show()
    sys.exit(Application.exec_())
