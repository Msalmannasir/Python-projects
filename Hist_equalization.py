import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rbg.jpeg', 0)

#counting bins
def bins_count(image, bins=256):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    return histogram

#cumulative sum
def cumsum(values):
    result = [values[0]]
    for i in values[1:]:
        result.append(result[-1] + i)
    return result

#Histogram Stretching
def stretch(entries):
    
    numerator = (entries - np.min(entries)) * 255
    denorminator = np.max(entries) - np.min(entries)
    result = numerator / denorminator
    return result

#Histogram equalization
def equalization(img):
    
    flatten_img = img.flatten()
    
    cumSum_r = cumsum(bins_count(flatten_img))  
    
    cumulativeSum_norm = stretch(cumSum_r)
    
    img_new_his = cumulativeSum_norm[flatten_img]
    
    img_new = np.reshape(img_new_his, img.shape)
    
    return img_new, cumulativeSum_norm 
                                        #equalized imaged returned to MAIN
                                        #normalized_cumsum returned to MAIN

#function to print the images
def drawImage(orignal, result, hist):

    fig, axes = plt.subplots(2, figsize=(10, 10))
    axes[0].imshow(orignal, cmap='gray')
    axes[0].set_title('Result before equalization')
    
    axes[1].imshow(result, cmap='gray')
    axes[1].set_title('Result after equalization')
    
    fig.savefig('Result.png')

#MAIN
result, normalized_cumsum = equalization(img)
    
drawImage(img, result, normalized_cumsum)