'''
Application of gardients in images 

Gradients here itself means partial derivatives.
Gradients are useful in detecting the edges based on color 
gradients.

Derivative of a matrix is calculated by an operator called Laplacian.

For derivatives, we have to cal. two derivatives, Sobal derivatives - one is horizontal, vertical.

This is some mathematical details, let's go to implementation.
'''

import cv2
import numpy as numpy
import matplotlib.pyplot as plt

img = cv2.imread('images/gradients1.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5)
cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobelx)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0)

plt.imshow(sobelx,cmap = 'gray')
plt.show()
plt.imshow(sobely,cmap = 'gray')

plt.show()
    