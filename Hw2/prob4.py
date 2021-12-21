from matplotlib import pyplot
from matplotlib import image
from sklearn.decomposition import PCA
import numpy as np

img_cnt=30
col_cnt=15

def prob4_1():
    for i in range(1,img_cnt+1):
        img = image.imread(f"Dataset_CvDl_Hw2/{i}.jpg")
        pyplot.subplot(4,col_cnt,i+(i>col_cnt)*col_cnt)
        pyplot.imshow(img)
        
        new_rgb=[]
        for j in range(4):
            pca = PCA(200)
            pca_img = pca.fit_transform(img[:,:,j])
            new_rgb.append(pca.inverse_transform(pca_img))

        new_img=np.stack(new_rgb,axis=2).astype("uint8")
        pyplot.subplot(4,col_cnt,i+col_cnt+(i>col_cnt)*col_cnt)
        pyplot.imshow(new_img)





        
    pyplot.show()
