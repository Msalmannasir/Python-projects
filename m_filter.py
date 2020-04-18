# import cv2 module
import cv2

# import numpy module as np
import numpy as np
from matplotlib import pyplot as plt

# Define a function for performing
# Median Blur on images
def MedianBlur(img,order) :
    bI = img
    for i in range(order//2 + 1, bI.shape[0]) :
        for j in range(order//2 +1, bI.shape[1]) :

            #making a sub-matrix in each iteration of size dependant of order
            matrix = bI[i-order//2: i+ order//2 + 1, j - order//2: j+ order//2 + 1]
            
            med = np.median(matrix)
            img[i, j] = med
            
    return img

def preWitt(img):
    #prewitt_horizontal
    pre_h = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    img_ph = cv2.filter2D(img, -1, pre_h)
    
    #prewitt_horizontal
    pre_v = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_pv = cv2.filter2D(img, -1, pre_v)
    return img_ph,img_pv


def drawImage(img, img1, imgh, imgv):
    fig, axes = plt.subplots(2,2, figsize=(10, 10))
    axes[0,0].imshow(img, cmap='gray')
    axes[0,0].set_title('before median')
        
    axes[0,1].imshow(img1, cmap='gray')
    axes[0,1].set_title('after median')
    
    axes[1,0].imshow(imgh, cmap='gray')
    axes[1,0].set_title('after prewitt(horizontal)')
    
    axes[1,1].imshow(imgv, cmap='gray')
    axes[1,1].set_title('after prewitt(vertical)')
    
    fig.savefig('Result.png')

#MAIN
oimg = cv2.imread("noisy.jpg",0)
img1 = cv2.imread("noisy.jpg",0)

# order of the submatrix
order = 5

#function calling
img1 = MedianBlur(img1,order)
img3 = img1
imgh,imgv =  preWitt(img1)
drawImage(oimg,img1,imgh,imgv)