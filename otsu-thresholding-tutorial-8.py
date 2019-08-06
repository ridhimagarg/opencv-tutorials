import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('images/otsu.jpg',0)

ret1, thesh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)


