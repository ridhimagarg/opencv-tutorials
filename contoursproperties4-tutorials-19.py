'''
Going to discuss some advanced properties
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/contours_tictactoe.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.shape,imgray.shape)

cv2.imshow('Original', img)
cv2.imshow('Grayed',imgray)
cv2.waitKey(0)

cnts, heir = cv2.findContours(imgray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,cnts,-1,(0,255,0),3)

cv2.imshow('Contours',img)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    #print(i,c)
    area = cv2.contourArea(c)
    (x,y,w,h) = cv2.boundingRect(c)
    print(i, area)

    hull = cv2.convexHull(c)
    hullarea = cv2.contourArea(hull)
    solidity = area/float(hullarea)

#print(cnts[0])