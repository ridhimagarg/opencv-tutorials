import cv2
import matplotlib.pyplot as pyplot
import numpy as np

img = cv2.imread('images/gradients3.png',0)

(t, binary) = cv2.threshold(img, thresh = 200, maxval = 255, type = cv2.THRESH_BINARY)

## Finding the contours
contours, hierarchy =  cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

M = cv2.moments(cnt)
print(M)

cx = int(M['m01']/M['m00'])
cy = int(M['m10']/M['m00'])

print(cx, cy)

## Let's use these calculated centroid values

cv2.imshow('Original', img)
cv2.waitKey(0)

x_axis = cx/2
y_axis = cy/2