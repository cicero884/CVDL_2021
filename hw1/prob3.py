import cv2
from matplotlib import pyplot

def prob3_1():
    imL = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imL.png')
    imR = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imR.png')
    imL_g=cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
    imR_g=cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)
    stereo = cv2.StereoBM_create(256,25)
    dpim=stereo.compute(imL_g, imR_g)
    #cv2.imshow('3.1 Result', dpim)
    pyplot.imshow(dpim, 'gray')
    pyplot.show()


def draw_point(event,x,y,flags,parameter):
    imR,dpim=parameter
    if event==cv2.EVENT_LBUTTONDOWN:
        print(y,x)
        print(dpim[y][x])
        if dpim[y][x] != -16:
            tmp_imR=imR.copy()
            cv2.circle(tmp_imR,(x-int(dpim[y][x]/16),y),20,(0,0,255),10)
            cv2.namedWindow("img2",0)
            cv2.resizeWindow("img2",700,700)
            cv2.imshow("img2",tmp_imR)

def prob3_2():
    imL = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imL.png')
    imR = cv2.imread(f'./Dataset_CvDl_Hw1/Q3_Image/imR.png')
    imL_g=cv2.cvtColor(imL, cv2.COLOR_BGR2GRAY)
    imR_g=cv2.cvtColor(imR, cv2.COLOR_BGR2GRAY)
    stereo = cv2.StereoBM_create(256,25)
    dpim=stereo.compute(imL_g, imR_g)
    print(imL.shape)
    print(dpim.shape)
    cv2.namedWindow("img1",0)
    cv2.resizeWindow("img1",700,700)
    cv2.imshow("img1",imL)
    cv2.setMouseCallback('img1',draw_point,(imR,dpim))
    
