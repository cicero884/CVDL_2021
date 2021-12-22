import cv2
import numpy as np

CHESS_SIZE=(11,8)
IMG_CNT=5

def shift_line(line,shift):
    for i in range(3):
        line[0][i]+=shift[i]
        line[1][i]+=shift[i]
    return line

def prob2(text,is_vertical):
    file_name='alphabet_lib_vertical.txt' if is_vertical else 'alphabet_lib_onboard.txt'
    fs = cv2.FileStorage(f'Dataset_CvDl_Hw1/Q2_Image/Q2_lib/{file_name}', cv2.FILE_STORAGE_READ)

    img=[]
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(10,7,0)
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(IMG_CNT):
        img.append(cv2.imread(f"Dataset_CvDl_Hw1/Q2_Image/{i+1}.bmp"))
        ret,corners=cv2.findChessboardCorners(img[i],CHESS_SIZE,None)
        if ret==True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img[0].shape[::-2], None, None)
    for i in range(IMG_CNT):
        for j in range(len(text)):
            ch=fs.getNode(text[j]).mat()
            for line in ch:
                line=shift_line(line,[7-j%3*3,5-int(j/3)*3,0])
                line=np.float32(line).reshape(-1,3)
                img_line, jac = cv2.projectPoints(line, rvecs[i], tvecs[i], mtx, dist)
                pt1=tuple(map(int,img_line[0].ravel()))
                pt2=tuple(map(int,img_line[1].ravel()))
                img[i]=cv2.line(img[i],pt1,pt2,(0,0,255),5)
        img[i]=cv2.resize(img[i], (720, 720))
        cv2.imshow('12x9 chessborad',img[i])
        cv2.waitKey(1000)
    cv2.destroyAllWindows()

