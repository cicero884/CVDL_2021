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
    model=prob5_train.construct_resnet50()
    print(model.summary())

def prob5_4():
    accuracy = image.imread('accuracy.png')
    loss = image.imread('loss.png')
    pyplot.imshow(accuracy)
    pyplot.show()
    pyplot.imshow(loss)
    pyplot.show()

def prob5_5(index):
    model=prob5_train.load_trained_model()
    if len(index)==0:
        model.evaluate(prob5_train.x_test,prob5_train.y_test)
        return
    index=int(index)
    
    predict = model.predict(prob5_train.x_test[index].reshape(-1, 32, 32, 3))

    testlebal = cifar_label[prob5_train.Y_test[index][0]]
    pyplot.title(testlebal)
    pyplot.imshow(prob5_train.x_test[index])
    pyplot.show()

    fig = pyplot.figure()
    x = numpy.arange(len(cifar_label))
    pyplot.bar(x, predict[0])
    pyplot.xticks(x, cifar_label)
    fig.set_figheight(6)
    fig.set_figwidth(10)
    pyplot.show()

