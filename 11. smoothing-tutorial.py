'''
Blur image with low pass filter.
Smoothing helps in reducing noise from image
It helps in creating less pixelated image.
In upcoming tutorial like canny edge detection, will see the use of smoothing techniques.

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

## Reading image
img = cv2.imread('images/opencv-logo.png')

## Creating the kernel for smoothening
## Creating array of 1 of size 5*5
kernel = np.ones((5,5), np.float32)/25

## Applying 2D convolution
smooth = cv2.filter2D(img, -1, kernel)

## Plotting the images
images = [img,smooth]
titles = ['Original', 'Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i]) 

plt.show()

'''
Performing average smoothening, Same as 
'''
avg_smooth = cv2.blur(img, (5,5))

images = [img,avg_smooth]
titles = ['Original', ' Average Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

## Gaussian Blurring
gaussian = cv2.GaussianBlur(img, (5,5), 0)

images = [img,gaussian]
titles = ['Original', 'Gaussian Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

## Median Smoothening to remove noise from image
img2 = cv2.imread('images/noisy4.jfif')

median = cv2.medianBlur(img2, 5)

images = [img2,median]
titles = ['Original', 'Median Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])
    
plt.show()
