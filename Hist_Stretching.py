import cv2 as cv
import numpy as np

img = cv.imread("flower.jpg",0)

def stretch(img):
    min = np.min(img)
    max = np.max(img)
    col,row = img.shape
    
    for i in range(0,col):
        for j in range(0,row):
            img[i][j] = ((img[i][j]-min)/(max-min))*255
            
    return img
img1 = stretch(img)        
cv.imwrite('stretched.jpg',img1)
