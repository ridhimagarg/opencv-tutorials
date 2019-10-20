import numpy as np 
import cv2
import matplotlib.pyplot as pyplot

img = cv2.imread('images/messi.jpg', 0)
img2 = img.copy()

template = cv2.imread('images/messi_face.jpg',0)

## [::-1] just to make width and height value interchange
w, h = template.shape[::-1]

print(w,h)

