'''
Application - extracting the foreground
by making background black.

How it works -:

- Initial a rectangle pixels is given by user and 
everything outside that rectangle is background and
everything inside it is considered as unknown.

- Using GMM, will decide this pizel comes in foreground
or background.

- 


'''

import cv2
import numpy as np 

img = cv2.imread('images/messi.jpg')

mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (50, 50, 450, 290)

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, mode=cv2.GC_INIT_WITH_RECT)

cv2.imshow('images', img)

cv2.imshow('mask', mask)
cv2.waitKey(0)

mask2 = np.where((mask ==2) | (mask== 0), 0, 1).astype('uint8')

img = img * mask2[:,:,np.newaxis]

cv2.imshow('final', img)
cv2.waitKey(0)