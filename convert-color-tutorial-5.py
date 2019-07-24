import cv2
import numpy as np

img  = cv2.imread('images/opencv-logo.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv",hsv)
cv2.waitKey(0)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow("mask",mask)
cv2.waitKey(0)

res = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow("res",res)
cv2.waitKey(0)