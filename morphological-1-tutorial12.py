'''
Morphological operations are broad set of operations in 
image processing

Erosion - erodes boundaries of foreground object.
Application - removing white noises and detach joint objects 

Dilation - opposite of erosion, generally erosion followed by dilation
Application- joining breaking parts

Opening - errosion followed by dilation

Closing - dilation followed by erosion
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('./images/morph1.png')

cv2.imshow('image',img)
cv2.waitKey(0)

kernel = np.ones((5,5), np.uint8)
## Performing opening operation to remove small objects from image
remove_small_objects = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('Opening', remove_small_objects)
cv2.waitKey(0)