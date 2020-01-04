'''
Application - Image segmentation basically is one of the application of 
this algorithm.

Due to noise and irregularities, we don't apply directly the watershed.

Steps:
We will try to find the sure background and sure foreground.
and mark the unknown area as the marker for watershed.

- Using dilation, will find out the sure background as it will make edges wider,
using opening, will do dilation.

- For sure foreground, we are using distance transform. 
Distance transform helps in detecting the distance from the defined edge,
here edge is the boundary.

- Then on the unkown area will apply the watershed algo.



'''

import cv2
import numpy as np 


img = cv2.imread('images/water_coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', gray)


## Applying dilation for sure_bg detection
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cnts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()

cv2.drawContours(img2,cnts,-1,(0,255,0),3)

cv2.imshow('contour', img2)

cv2.waitKey(0)

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow('Open', opening)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

## Sure background image
cv2.imshow('dilated', sure_bg)

## Cjecking what if simple threshlded image is dilated (Otional)
bg = cv2.dilate(thresh, kernel, iterations=3)

cv2.imshow('bg', bg)

## Foreground extraction
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)


sure_fg = np.uint8(sure_fg)

## The unknown area is between sure background and sure foreground
unknown = np.subtract(sure_bg, sure_fg)

cv2.imshow('unknown', unknown)


ret, markers = cv2.connectedComponents(sure_fg)

print(markers)

## Add one so that sure background is not 1
markers = markers +1

## Making the unknown area as 0
markers[unknown == 255] = 0

#cv2.imshow('markers2', markers)

cv2.waitKey(0)

markers = cv2.watershed(img, markers)

## boundary region is marked with -1
img[markers == -1] = (255, 0, 0)

cv2.imshow('watershed',img)

cv2.waitKey(0)