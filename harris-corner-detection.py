import cv2
import numpy as np

img = cv2.imread('images/chessboard.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)

## For displaying the corners properly, making more boundaries
dst = cv2.dilate(dst, None)

## applying threshold for optimal value.
img[dst> 0.01*dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)

cv2.waitKey(0)
