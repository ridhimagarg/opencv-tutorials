'''
Going to discuss some advanced properties.
How to use solidity property to distingush between 'X' and '0' in tictactoe image

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/contours_tictactoe.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.shape,imgray.shape)

## Showing up Original and gray image
cv2.imshow('Original', img)
cv2.imshow('Grayed',imgray)
cv2.waitKey(0)

## First finding the contours
cnts, heir = cv2.findContours(imgray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

## You can uncomment it if you want to see the full list of contours


# cv2.drawContours(img,cnts,-1,(0,255,0),3)

# cv2.imshow('Contours',img)
# cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    #print(i,c)
    area = cv2.contourArea(c)
    (x,y,w,h) = cv2.boundingRect(c)
    print(i, area)

    hull = cv2.convexHull(c)
    hullarea = cv2.contourArea(hull)
    solidity = area/float(hullarea)
    print(solidity)

    char = '?'

    ## solidity value: 0.8 for "0" because it has less concexity defect 
    if solidity > 0.8:
        char = '0'

    ## solidity cvalue: 0.5 for "X" as it has higher convexity so less solidity value.   
    elif solidity > 0.5:
        char = 'X'

    ## Drawing contour and put text of detected shape
    if char != '?':
        cv2.drawContours(img, [c], -1, (0,255,0), 3)
        cv2.putText(img, char, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 255, 0), 4)


cv2.imshow('Output',img)
cv2.waitKey(0)
#print(cnts[0])