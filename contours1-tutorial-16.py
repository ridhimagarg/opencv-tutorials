'''

Contours are a curve joining all the continous points having same intensity(color).

Performing the find contour, try to convert image into binary.


'''

import cv2
import matplotlib.pyplot as pyplot
import numpy as np

img = cv2.imread('images/gradients.jpg')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
