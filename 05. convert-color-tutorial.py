'''
How to convert color of image in opencv and finding out the region of particular color only

'''

import cv2
import numpy as np

## Reading images
img  = cv2.imread('images/opencv-logo.png')

## Converting it to HSV as it will detect color more accurately
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## Showing up the converted hsv image
cv2.imshow("hsv",hsv)
cv2.waitKey(0)

## Defining the range for blue color
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

## Checking if the hsv image is in this range so that it will 
## black out other parts from blue one
mask = cv2.inRange(hsv, lower_blue, upper_blue)

## Showing up the masked image
cv2.imshow("mask",mask)
cv2.waitKey(0)

## Now performing "and" operation to get the blue color only.  
res = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow("Only blue",res)
cv2.waitKey(0)

## Here we are trying to convert the background from black to white
## mask ==0 means black pixels wherever mask value is 0 will replace with white
res[mask == 0] = (255, 255, 255)
cv2.imshow("Convert black to white",res)
cv2.waitKey(0)