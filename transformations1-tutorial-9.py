import cv2
import numpy as numpy

images = ['DL-1.png','DL-2.jpg', 'DL-3.jpg']

for im in images:

    img = cv2.imread('images/'+str(im))

    height, width = img.shape[:2]

    if height <505 and width <795:
        res = cv2.resize(img, (795, 505), interpolation= cv2.INTER_CUBIC)

        cv2.imshow('original', img)
        cv2.waitKey(0)

        cv2.imshow('resized',res)
        cv2.waitKey(0)