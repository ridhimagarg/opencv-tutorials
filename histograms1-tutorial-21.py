import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/contours_hierarchy.png')

hist = cv2.calcHist([img],[0],None,[256],[0,256])

print(hist)

print(hist.shape)