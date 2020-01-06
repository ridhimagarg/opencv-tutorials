'''
In this will see Ostu's thresholding and it difference with Thresholding binary.

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('images/otsu.jpg',0)

## Simple binary thresholding
ret1, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

## Binary thresholding with ostu thresholding
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

## Performing Gassian Blurring and then binary+ostu thresholding
gauss_img = cv2.GaussianBlur(img, (5,5), 0)
ret3, thresh3 = cv2.threshold(gauss_img, 127,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


## Checking all the thresholding outputs
images = [thresh1, thresh2, thresh3]

titles = ['Global Thresholding (v=127)', "Otsu's Thresholding", "Otsu's Thresholding with Gaussian Blur"]

## Showing up all different results in to one graph
for i in range(3):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()