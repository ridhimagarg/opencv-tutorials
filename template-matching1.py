import numpy as np 
import cv2
import matplotlib.pyplot as pyplot

img = cv2.imread('images/messi.jpg', 0)
img2 = img.copy()

template = cv2.imread('images/messi_face.jpg',0)

## [::-1] just to make width and height value interchange
w, h = template.shape[::-1]

print(w,h)

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    res = cv2.matchTemplate(img, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    

