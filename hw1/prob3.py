import cv2
from matplotlib import pyplot

def get_sterio():
    imL = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imL.png')
    imR = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imR.png')
    imL_g=cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
    imR_g=cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)
    stereo = cv2.StereoBM_create(256,25)
    return stereo.compute(imL_g, imR_g)


def prob3_1():
    dpim=get_sterio()
    cv2.imshow('3.1 Result', dpim)
    pyplot.imshow(dpim, 'gray')
    pyplot.show()

def prob3_2():
    dpim=get_sterio()

