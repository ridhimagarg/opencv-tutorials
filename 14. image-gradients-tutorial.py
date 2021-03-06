'''
Application of gardients in images 

Gradients here itself means partial derivatives.
Gradients are useful in detecting the edges based on color 
gradients.

Derivative of a matrix is calculated by an operator called Laplacian.

For derivatives, we have to calculate two derivatives, Sobal derivatives - one is horizontal, vertical.

This is some mathematical details, let's go to implementation.
'''

import cv2
import numpy as numpy
import matplotlib.pyplot as plt

img = cv2.imread('images/gradients4.jpg',0)

## Applying laplacian 
laplacian = cv2.Laplacian(img, cv2.CV_64F)

## Applying sobel filters for x and y direction
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5)

## Showing up all the images
images = [img, laplacian, sobelx, sobely]
titles = ['Original', 'Laplacian', 'SobelX', 'SobelY']

for i in range(4):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])

plt.show()

## Applying filters on other iamges
img = cv2.imread('images/gradients2.jpg',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5)

images = [img, laplacian, sobelx, sobely]
titles = ['Original', 'Laplacian', 'SobelX', 'SobelY']

## Plotting into two different ways
for i in range(4):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])

plt.show()

for i in range(4):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()



    