import cv2
import numpy as np 


img = cv2.imread('images/water_coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', gray)

cv2.waitKey(0)


