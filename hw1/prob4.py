import cv2
import numpy
from matplotlib import pyplot

def prob4_1():
    img1=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark1.jpg')
    img2=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark2.jpg')
    
    sift=cv2.SIFT_create()
    kp1,des1=sift.detectAndCompute(img1,None)
    kp2,des2=sift.detectAndCompute(img2,None)

    kp1=sorted(kp1, key=lambda keypoint: keypoint.size, reverse=True)[:200]
    kp2=sorted(kp2, key=lambda keypoint: keypoint.size, reverse=True)[:200]

    draw_params=dict(flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img1=cv2.drawKeypoints(gray_img1,kp1,img1,**draw_params)
    img2=cv2.drawKeypoints(gray_img2,kp2,img2,**draw_params)

    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)

    cv2.imwrite('Q4_Image/FeatureAerial1.jpg',img1)
    cv2.imwrite('Q4_Image/FeatureAerial2.jpg',img2)

def prob4_2():
    img1=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark1.jpg')
    img2=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark2.jpg')
    
    sift=cv2.SIFT_create()

    kp1,des1=sift.detectAndCompute(img1,None)
    kp2,des2=sift.detectAndCompute(img2,None)
    kp1,des1=(list(t) for t in zip(*sorted(zip(kp1,des1), key=lambda pair: pair[0].size, reverse=True)))
    kp1=numpy.asarray(kp1[:200])
    des1=numpy.asarray(des1[:200])
    kp2,des2=(list(t) for t in zip(*sorted(zip(kp2,des2), key=lambda pair: pair[0].size, reverse=True)))
    kp2=numpy.asarray(kp2[:200])
    des2=numpy.asarray(des2[:200])

    draw_params = dict(
        color = (0,0,255),
        flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img1=cv2.drawKeypoints(gray_img1,kp1,img1,**draw_params)
    img2=cv2.drawKeypoints(gray_img2,kp2,img2,**draw_params)

    matcher=cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)
    matches=matcher.knnMatch(des1,des2,2)

    good=[]
    for i,(m1,m2) in enumerate(matches):
        if m1.distance < 0.55 * m2.distance:
            good.append([m1])

    draw_params=dict(
        matchColor=(0,255,0),
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,**draw_params)
    pyplot.imshow(img3)
    pyplot.show()

def prob4_3():
    img1=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark1.jpg')
    img2=cv2.imread(f'Dataset_CvDl_Hw1/Q4_Image/Shark2.jpg')
    
    sift=cv2.SIFT_create()

    kp1,des1=sift.detectAndCompute(img1,None)
    kp2,des2=sift.detectAndCompute(img2,None)
    kp1,des1=(list(t) for t in zip(*sorted(zip(kp1,des1), key=lambda pair: pair[0].size, reverse=True)))
    kp1=numpy.asarray(kp1[:200])
    des1=numpy.asarray(des1[:200])
    kp2,des2=(list(t) for t in zip(*sorted(zip(kp2,des2), key=lambda pair: pair[0].size, reverse=True)))
    kp2=numpy.asarray(kp2[:200])
    des2=numpy.asarray(des2[:200])

    matcher=cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)
    matches=matcher.knnMatch(des1,des2,2)

    good1=[]
    good2=[]
    for i,(m1,m2) in enumerate(matches):
        if m1.distance < 0.55 * m2.distance:
            good1.append(m1)
            good2.append(m2)
    kp1=numpy.float32([ kp1[m.queryIdx].pt for m in good1 ]).reshape(-1,1,2)
    kp2=numpy.float32([ kp2[m.trainIdx].pt for m in good1 ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(kp2, kp1, cv2.RANSAC)
    img2_s=cv2.warpPerspective(img2, M, (2*img1.shape[1],2*img1.shape[0]))

    img2_s[:img1.shape[0],:img1.shape[1]]=img1
    gray_img=cv2.cvtColor(img2_s, cv2.COLOR_BGR2GRAY)
    cv2.imshow("result",gray_img)
