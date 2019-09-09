'''
Going to discuss some advanced properties.

Application Resource -> https://gurus.pyimagesearch.com/lesson-sample-advanced-contour-properties/

How to use solidity property to distingush between 'X' and '0' in tictactoe image

1. Aspect Ratio -> width/height
2. Extent -> Object Area/ Bounding Rect area

Aspect ratio(AR) can be used to detect shape like square and circle most probably have AR as 1.
Extent can aslo be used for shape detection.

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt 


##------------------------------------------ First Application --------------------------##

img = cv2.imread('images/contours_tictactoe.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.shape,imgray.shape)

## Showing up Original and gray image
cv2.imshow('Original', img)
cv2.imshow('Grayed',imgray)
cv2.waitKey(0)

## First finding the contours
cnts, heir = cv2.findContours(imgray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

## You can uncomment it if you want to see the full list of contours


# cv2.drawContours(img,cnts,-1,(0,255,0),3)

# cv2.imshow('Contours',img)
# cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    #print(i,c)
    area = cv2.contourArea(c)
    (x,y,w,h) = cv2.boundingRect(c)
    print(i, area)

    hull = cv2.convexHull(c)
    hullarea = cv2.contourArea(hull)
    solidity = area/float(hullarea)
    print(solidity)

    char = '?'

    ## solidity value: 0.8 for "0" because it has less concexity defect 
    if solidity > 0.8:
        char = '0'

    ## solidity cvalue: 0.5 for "X" as it has higher convexity so less solidity value.   
    elif solidity > 0.5:
        char = 'X'

    ## Drawing contour and put text of detected shape
    if char != '?':
        cv2.drawContours(img, [c], -1, (0,255,0), 3)
        cv2.putText(img, char, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 255, 0), 4)


cv2.imshow('Output',img)
cv2.waitKey(0)
#print(cnts[0])




##-------------------------------- Second Application ---------------------------##

img = cv2.imread('images/contours_tetris_blocks.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(imgray, 225, 255, cv2.THRESH_BINARY_INV)

cnts, heir = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

hullimage = np.zeros(imgray.shape[:2], dtype="uint8")

for (i,c) in enumerate(cnts):

    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    aspectRatio = w / float(h)

    extent = area / float(w * h)

    hull = cv2.convexHull(c)

    hullarea = cv2.contourArea(hull)
    solidity = area/ float(hullarea)

    cv2.drawContours(hullimage, [hull], -1, 255, -1)
    cv2.drawContours(img, [c], -1, (240, 0, 159), 3)

    shape = ""

    if aspectRatio >= 0.98 and aspectRatio <= 1.02:
        shape = "SQUARE"

    

for (i, c) in enumerate(cnts):


	# compute the area of the contour along with the bounding box
	# to compute the aspect ratio
	area = cv2.contourArea(c)
	(x, y, w, h) = cv2.boundingRect(c)
 
	# compute the aspect ratio of the contour, which is simply the width
	# divided by the height of the bounding box
	aspectRatio = w / float(h)
 
	# use the area of the contour and the bounding box area to compute
	# the extent
	extent = area / float(w * h)
 
	# compute the convex hull of the contour, then use the area of the
	# original contour and the area of the convex hull to compute the
	# solidity
	hull = cv2.convexHull(c)
	hullarea = cv2.contourArea(hull)
	solidity = area / float(hullarea)
 
	# visualize the original contours and the convex hull and initialize
	# the name of the shape
	cv2.drawContours(hullimage, [hull], -1, 255, -1)
	cv2.drawContours(img, [c], -1, (240, 0, 159), 3)

	#shape = ""

    if aspectRatio >= 0.98:
        shape = "SQUARE"


    # if (aspectRatio >= 0.98 and aspectRatio <= 1.02):
    #     shape = "SQUARE"

    # # if the width is 3x longer than the height, then we have a rectangle
    # elif aspectRatio >= 3.0:
    #     shape = "RECTANGLE"

    # # if the extent is sufficiently small, then we have a L-piece
    # elif extent < 0.65:
    #     shape = "L-PIECE"

    # # if the solidity is sufficiently large enough, then we have a Z-piece
    # elif solidity > 0.80:
    #     shape = "Z-PIECE"

    # # draw the shape name on the image
    # cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
    #     (240, 0, 159), 2)

    # # show the contour properties
    # print("Contour #{} -- aspect_ratio={:.2f}, extent={:.2f}, solidity={:.2f}"
    #     .format(i + 1, aspectRatio, extent, solidity))
 
# show the output images

cv2.imshow("Convex Hull", hullimage)
cv2.imshow("Image", img)
cv2.waitKey(0)


