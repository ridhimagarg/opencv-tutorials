import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/messi.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0 , 256])


print(hist)
print(hist.shape)

plt.imshow(hist, interpolation='nearest')
plt.show()

## histogram backprojection

roi = cv2.imread('images/roi.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


target = cv2.imread('images/target.jpg')
hsvt = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

M = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt], [0,1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(M, interpolation='nearest')
plt.imshow(I, interpolation='nearest')

plt.show()
