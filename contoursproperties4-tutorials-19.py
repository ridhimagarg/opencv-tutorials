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

cnts = cv2.findContours(imgray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for (i, c) in enumerate(cnts):
    print(i,c)