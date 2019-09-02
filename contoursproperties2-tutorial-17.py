import cv2
import matplotlib.pyplot as pyplot
import numpy as np

img = cv2.imread('images/gradients3.png')

#(t, binary) = cv2.threshold(img, thresh = 200, maxval = 255, type = cv2.THRESH_BINARY)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)

## Finding the contours
contours, hierarchy =  cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

print(np.array(contours).shape)

cnt = contours[0]

M = cv2.moments(cnt)
print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx, cy)

## Let's use these calculated centroid values

cv2.imshow('Original', img)


x_axis = cx/2
y_axis = cy/2

start_x = int(cx/2)
end_x = int(start_x + cx)

start_y = int(cy/2)
end_y = int(start_y + cy)

print(start_x, start_y, end_x, end_y)


new_img = img[start_y:end_y, start_x:end_x]
print(img.shape)

cv2.imshow('new',new_img)
cv2.waitKey(0)