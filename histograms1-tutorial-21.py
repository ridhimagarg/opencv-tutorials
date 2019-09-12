import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('images/contours_hierarchy.png')

## here [0] means gray scale image
## If colored image, pass [0], [1], [2] for b,g,r
hist = cv2.calcHist([img],[0],None,[256],[0,256])

print(hist)

print(hist.shape)

## Plotting histograms
plt.hist(img.ravel(), 256, [0,256])

## In this picture we have only black and white pixels so 0(black) and 255(white-bright) has high(all) numbers
plt.show()

img = cv2.imread('images/messi.jpg',0)

cv2.imshow('Original', img)


hist, bins = np.histogram(img, 256, [0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * hist.max() / cdf.max()

# plt.plot(cdf_normalized, color ='b')
# plt.hist(img.ravel(), 256, [0,256], color='r')
# plt.show()

equ = cv2.equalizeHist(img)
cv2.imshow('Equalized',equ)

cv2.waitKey(0)

