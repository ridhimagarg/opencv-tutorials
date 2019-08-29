'''
In previous code snippet discussed abot image gradient
method for edge detection. In this snippet will look for more
advanced canny edge detector algo.

This is into 4 phases 

Noise Reduction -> Finding gradient direction and magnitude -> Non-max supression -> Hystresis Thresholding.

In Noise reduction, remove noise using smoothing filters like gaussian.

Finding gradient magnitude -> Using first derivative i.e, Sobel filters will find the direction (angle between horizontal and vertical derivative)
And magnitude using both horiz and vetical  = np.sqrt(Sx**2 + Sy**2)

Non-max supression -> Basically a first stage filtering for non-edges.

Hystersis thresholding -> Using range for maxval and minval, filter edges and non-edges
'''

import cv2
import numpy as np 
import matplotlib.pyplot as pyplot
