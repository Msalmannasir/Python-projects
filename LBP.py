import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def lbp(image,x,y,P,R):
    sum=0
    if(P==8):
        temp = np.zeros((3,3),int)
        temp[1][1] =  image[x][y]
        if(temp[1][1] <= image[x-R][y+R]):
            temp[0][2] = 1
        else:
            temp[0][2] = 0
        if(temp[1][1] <= image[x][y+R]):
            temp[1][2] = 1
        else:
            temp[1][2] = 0
        if(temp[1][1] <= image[x+R][y+R]):
            temp[2][2] = 1
        else:
            temp[2][2] = 0
        if(temp[1][1] <= image[x+R][y]):
            temp[2][1] = 1
        else:
            temp[2][1] = 0
        if(temp[1][1] <= image[x+R][y-R]):
            temp[2][0] = 1
        else:
            temp[2][0] = 0
        if(temp[1][1] <= image[x][y-R]):
            temp[1][0] = 1
        else:
            temp[1][0] = 0
        if(temp[1][1] <= image[x-R][y-R]):
            temp[0][0] = 1
        else:
            temp[0][0] = 0
        if(temp[1][1] <= image[x-R][y]):
            temp[0][1] = 1
        else:
            temp[0][1] = 0
    #NOWTOCALCULATESUM
        if(temp[0][2] == 1):
            sum = sum + temp[0][2]*(2^7)
        if(temp[1][2] == 1):
            sum = sum + temp[1][2]*(2^6)
        if(temp[2][2] == 1):
            sum = sum + temp[2][2]*(2^5)
        if(temp[2][1] == 1):
            sum = sum + temp[2][1]*(2^4)
        if(temp[2][0] == 1):
            sum = sum + temp[2][0]*(2^3)
        if(temp[1][0] == 1):
            sum = sum + temp[1][0]*(2^2)
        if(temp[0][0] == 1):
            sum = sum + temp[0][0]*(2^1)
        if(temp[0][1] == 1):
            sum = sum + 1
    return sum

image = cv.imread("img.jpg",2)
newimage = image
col,row = image.shape
for i in range(1,col-1):
    for j in range(1,row-1):
       newimage[i][j] = lbp(image,i,j,8,1)
       if(newimage[i][j] < 100):
           newimage[i][j] = newimage[i][j] + 60

cv.imshow('',newimage)
cv.waitKey(0)
cv.destroyAllWindows()