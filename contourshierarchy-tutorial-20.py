import cv2
import numpy as np 
import matplotlib.pyplot as plt 


img = cv2.imread('images/contours_hierarchy.png',0)
cv2.imshow("ori", img)
cv2.waitKey(0)

#imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

cnts, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print(hier)


