'''
In previous code snippet discussed abot image gradient
method for edge detection. In this snippet will look for more
advanced canny edge detector algo.

This is into 4 phases 

Noise Reduction -> Finding gradient direction and magnitude -> Non-max supression -> Hystresis Thresholding.



'''

import cv2
import numpy as np 
import matplotlib.pyplot as pyplot
