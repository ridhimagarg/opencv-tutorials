import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/contour-approx1.jpg')

cv2.imshow('Original', img)
cv2.waitKey(0)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)

## Finding the contours
contours, hierarchy =  cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

## Finding centroid of first contour only
cnt = contours[0]

epsilon = cv2.arcLength(cnt,True) 
approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.drawContours(img,approx,-1,(0,255,0),3)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow('Approx', approx)
# cv2.waitKey(0)