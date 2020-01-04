'''
Application - extracting the foreground
by making background black.

How it works -:

- Initial a rectangle pixels is given by user and 
everything outside that rectangle is background and
everything inside it is considered as unknown.

- Using GMM, will decide this pizel comes in foreground
or background.

- Now create two new nodes, source and sink.
Foreground nodes are connected to souce node.
Background nodes are connecred to sink node.

- These edges contains weights depends upon the pixel similarity.

- And iterate and find out if this pixe should belong to source or sink node.

- Finally mincut algorithm is used to cut the graph into 
two separating nodes -: sink and source based on mimimum cost(distance).


'''

import cv2
import numpy as np 

img = cv2.imread('images/messi.jpg')

mask = np.zeros(img.shape[:2], np.uint8)

## Creating simple bg and fg model.
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (50, 50, 450, 290)

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, mode=cv2.GC_INIT_WITH_RECT)

cv2.imshow('images', img)

cv2.imshow('mask', mask)
cv2.waitKey(0)

## Making mask =2 and mask =0 as background and 1 and 3 as foreground.
mask2 = np.where((mask ==2) | (mask== 0), 0, 1).astype('uint8')

## Mapping this new mask to image
img = img * mask2[:,:,np.newaxis]

## Displaying image
cv2.imshow('final', img)
cv2.waitKey(0)