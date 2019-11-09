'''
Hough lines is used to detect shapes in image, if shape can be represented in mathematical form.

Line equation in parametric form --> rho = x* cos(theta) + y* sin(theta)

Short- alogrithm

    1. Loop over all the points on that line.
    2. For every point will find value of rho for every x and theta
    3. Increment the accumulator for (x, theta) and will point out those having high value.
'''


import cv2
import numpy as np

img = cv2.imread('images/gradients4.jpg')



## Converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#gaussian = cv2.GaussianBlur(gray, (3,3), 0)

## Detecting edges
edges = cv2.Canny(gray, 50, 150, apertureSize= 3)

## The algorithm we have seen is encapsulated in this function
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

## Looping over rho and theta
for i in  range(0,lines.shape[0]):

    rho,theta = lines[i,0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    ## Converting the parametric eqn into cartesian as image points in a cartesian plane.
    ## 1000 is been choosen as a random value. You can choose some big value like this also.
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('images',img)
cv2.waitKey(0)
cv2.imwrite('houghlines.jpg', img)

'''
Modified version of hough transform is probablistic hough transform, as hough transform does lots of
computation while this will select random number of lines which is sufficient for line detection.

It takes two more parameters in houghlinesP() function -:

1. minlength => Line shorter than this length will be rejected.
2. maLineGap => Max gap between two lines in order to treat them as separate line.


'''

img = cv2.imread('images/gradients4.jpg')

## Converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#gaussian = cv2.GaussianBlur(gray, (3,3), 0)

## Detecting edges
edges = cv2.Canny(gray, 50, 150, apertureSize= 3)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,10)

for i in  range(0,lines.shape[0]):
    x1, y1, x2, y2 = lines[i,0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('images',img)
cv2.waitKey(0)

'''
Hough circle transform

Equation of a circle -> (x - xcenter)^2 + (y - ycenter)^2

'''
img = cv2.imread('images/detect_circles.jpg',0)

img = cv2.medianBlur(img, 5)

## Converting to gray scale
#cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(img, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
	cv2.imshow("output", np.hstack([img, img]))
	cv2.waitKey(0)


#cv2.imshow('detected circles',cimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



