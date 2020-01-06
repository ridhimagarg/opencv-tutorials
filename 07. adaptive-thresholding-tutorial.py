''''

Here will see how adaptive thresholding works with the difference
between binary thresholding(commonly used thresholding). Here we are using simple function.
Later on I will try to demonstarte some real examples where it can comes into picture.

'''

## Note -: Sometimes in Opencv you need to make hit and trial whether to apply this function and tweaking the parameters

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/image8.jpg')

## Converting BGR to Gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Performing the median Blurring
img = cv2.medianBlur(img,5)

## Just to display blurred image
cv2.imshow('blurred',img)
cv2.waitKey(0)

## Performing simple thresholding
## Performing adaptive mean and gaussian thresholding
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img, 255,\
     cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)
thresh3 = cv2.adaptiveThreshold(img, 255,\
     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2) 

## Dispalying all types of thresholding
images = [thresh1, thresh2, thresh3]
titles = ['Binary', 'Adaptive mean', 'Adaptive Gaussian']

for i in range(3):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()