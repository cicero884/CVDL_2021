import cv2
import numpy as np

CHESS_SIZE=(11,8)

def prob1_1():
    for i in range(1, 15):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{i}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE)
        if ret==True:
            cv2.drawChessboardCorners(img,CHESS_SIZE,corners,ret)
            cv2.imshow('12x9 chessborad', img)
            cv2.waitKey(500)
    cv2.destroyAllWindows()

def prob1_2():
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(10,7,0)
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(1, 15):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{i}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE,None)
        if ret==True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-2], None, None)
    print("Intrinsic:")
    print(mtx)


def prob1_3(img_index):
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)
    img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{img_index}.bmp")
    ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE,None)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera([objp], [corners], img.shape[::-2], None, None)
    rvecs = cv2.Rodrigues(rvecs[0])
    print("Extrinsic:")
    print(np.append(rvecs[0],tvecs[0],axis=1))

def prob1_4():
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(10,7,0)
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(1, 15):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{i}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE,None)
        if ret==True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-2], None, None)
    print("Distortion:")
    print(dist[0])

def prob1_5():
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    #for i in range(1, 15):
    i=12
    img=cv2.imread(f"Dataset_CvDl_Hw1/Q1_Image/{i}.bmp")
    ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE)
    if ret==True:
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera([objp], [corners], img.shape[::-2], None, None)
        h,  w = img.shape[:2]
        print(h,w)
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
        # undistort
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        cv2.imshow('12x9 chessborad', dst)
        cv2.waitKey(500)
    cv2.destroyAllWindows()

