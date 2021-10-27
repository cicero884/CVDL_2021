import cv2

def prob2_1(text):
    img=[]
    fs = cv2.FileStorage(f'Dataset_CvDl_Hw1/Q2_Image/Q2_lib/alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(10,7,0)
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(5):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q2_Image/{i+1}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE,None)
        if ret==True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-2], None, None)
    
    

def prob2_2(text):
    img=[]
    fs = cv2.FileStorage(f'Dataset_CvDl_Hw1/Q2_Image/Q2_lib/alphabet_lib_vertical.txt', cv2.FILE_STORAGE_READ)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(10,7,0)
    objp = np.zeros((11*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(5):
        img=cv2.imread(f"Dataset_CvDl_Hw1/Q2_Image/{i+1}.bmp")
        ret,corners=cv2.findChessboardCorners(img,CHESS_SIZE,None)
        if ret==True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-2], None, None)
