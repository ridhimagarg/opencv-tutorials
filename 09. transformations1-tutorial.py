'''
Transformation application like resizing, transformed plane wise an image.

'''

import cv2
import numpy as np

## resizing images based on the original height and width
images = ['DL-1.png','DL-2.jpg', 'DL-3.jpg']

for im in images:

    img = cv2.imread('images/'+str(im))

    height, width = img.shape[:2]

    print(height, width)

    ## if height is less than 505 and width is greater than 795
    if height <505 and width <795:

        ## resizing image 
        ## interpolation of different types like cv2.INTER_AREA for shrinking, cv2.INTER_LINEAR for zooming etc.
        ## More details you can check documentation
        res = cv2.resize(img, (795, 505), interpolation= cv2.INTER_CUBIC)

        cv2.imshow('original', img)
        cv2.waitKey(0)

        cv2.imshow('resized',res)
        cv2.waitKey(0)

## Reading another image to perform transformation on the plane basis.
img = cv2.imread('images/image8.jpg')

height, width = img.shape[:2]

## You need to create transformation matrix in which tx and ty will change in this -: [[1,0,tx],[0.1, ty]]
## This will shift 100 towards x and 50 towards y
M = np.float32([[1,0,100],[0,1,50]])

## Use warpAffine transformation
## Adding some term in width and height, just to make look large
trs = cv2.warpAffine(img, M, (width+100,height+50) )

cv2.imshow('translated without shifting',trs)
cv2.waitKey(0)

## Again translate to make it look properly in middle.
M = np.float32([[1,0,-50],[0,1,-25]])
trs1 = cv2.warpAffine(trs, M, (width+100+50,height+50+25) )

cv2.imshow('Final translated',trs1)
cv2.waitKey(0)

## Performing affine transformation inorder to make image tilt plane wise.
## Use case could be if smome image is not align properly.
img = cv2.imread('images/image8.jpg')

height, width, ch = img.shape

## You need to play with these points in order to get proper shifting according to your requirement.
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1, pts2)

trs = cv2.warpAffine(img, M, (width, height))

cv2.imshow('Original',img)

cv2.imshow('Affine Transform',trs)
cv2.waitKey(0)
