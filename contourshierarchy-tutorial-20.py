import cv2
import numpy as np 
import matplotlib.pyplot as plt 


img = cv2.imread('images/contours_hierarchy.png')
cv2.imshow("ori", img)
cv2.waitKey(0)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh = cv2.threshold(imgray, 10, 255, cv2.THRESH_BINARY)

cnts, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, cnts, -1, (0,255,0), 1)

for (i,c) in enumerate(cnts):

    (x, y, w, h) = cv2.boundingRect(c)

    cv2.putText(img, str(i), (x+int(h/2), y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (240, 0, 159), 2 )

print(hier)

cv2.imshow("ori", img)
cv2.waitKey(0)


