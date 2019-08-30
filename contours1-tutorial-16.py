'''

Contours are a curve joining all the continous points having same intensity(color).

Performing the find contour, try to convert image into binary.


'''

import cv2
import matplotlib.pyplot as pyplot
import numpy as np

img = cv2.imread('images/gradients3.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', imgray)
cv2.waitKey(0)

ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy =  cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('contours',img)
cv2.waitKey(0)

print(np.array(contours).shape)