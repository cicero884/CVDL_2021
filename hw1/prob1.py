import cv2
import numpy as np

CHESS_SIZE=(11,8)

def prob1_1(self):
    print("here")
    for i in range(1, 15):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{i}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE)
        if ret==True:
            #cv2.cornerSubPix
            cv2.drawChessboardCorners(img,CHESS_SIZE,corners,ret)
            cv2.imshow('12x9 chessborad', img)
            cv2.waitKey(500)
    cv2.destroyAllWindows()
