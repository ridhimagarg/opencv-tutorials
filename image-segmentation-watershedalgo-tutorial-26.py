import cv2
import numpy as np 


img = cv2.imread('images/water_coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', gray)



ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow('Open', opening)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

cv2.imshow('dilated', sure_bg)

bg = cv2.dilate(thresh, kernel, iterations=3)

cv2.imshow('bg', bg)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)


sure_fg = np.uint8(sure_fg)

unknown = np.subtract(sure_bg, sure_fg)

cv2.imshow('unknown', unknown)

cv2.waitKey(0)