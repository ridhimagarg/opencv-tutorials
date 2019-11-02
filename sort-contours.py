import cv2
import numpy as np 

img = cv2.imread('images/contour_sort1.jpg')

accumEdged = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow('image', img)
cv2.waitKey(0)

#imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(img, 11)

edged = cv2.Canny(blur, 50, 200)

accumEdged = cv2.bitwise_or(accumEdged, edged)
# (t, binary) =  cv2.threshold(imgray, thresh=30, maxval= 255, type = cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(accumEdged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (255,0,0), 1)

cv2.imshow('image', accumEdged)
cv2.waitKey(0)

cv2.imshow('image', img)
cv2.waitKey(0)
#print(np.array(contours).shape)

def draw_contour(image, c, i):
    M = cv2.moments(c)
    cx = int(M["m10"]/ M["m00"])
    cy = int(M["m01"]/M["m00"])

    cv2.putText(image, "#{}".format(i+1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    return image
    
def sort_contours(cnts, method="left-to-right"):

    reverse = False
    i =0

    if method == 'right-to-left' or method == 'bottom-to-top':
        reverse = True

    if method == 'top-to-bottom' or method == 'bottom-to-top':
        i = 1

    boundingBoxes = [cv2.boundingRect(c) for c in cnts] 

    print(boundingBoxes)

    print(zip(cnts, boundingBoxes))

    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))

    
    return (cnts, boundingBoxes)

    

sort_contours(contours)

cnts, hier = cv2.findContours(accumEdged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]

orig = img.copy()

for (i,c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)

cv2.imshow("Unsorted", orig)

(cnts, boundingBoxes) = sort_contours(cnts, method="top-to-bottom")
 
# loop over the (now sorted) contours and draw them
for (i, c) in enumerate(cnts):
	draw_contour(img, c, i)
 
# show the output image
cv2.imshow("Sorted", img)
cv2.waitKey(0)
