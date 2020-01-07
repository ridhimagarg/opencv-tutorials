# opencv-tutorials
In this repository I will try to give good demos or small projects on open-cv functionalities


## 02. drawing-shapes-tutorial

We can draw different type of shapes like line, circle, eclipse, etc using opencv function like -:

- cv2.line()
  
<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img1.PNG'>

- cv2.rectangle()

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img2.PNG'>

## 03. callbacks-tutorial.py

Using callbacks, we can perform defined operations like cropping image etc. We can define mouse callback.

- cv2.setMouseCallback()

## 04. bitwise-op-tutorial.py

Using bitwise or, and will manipulate image to find out the mask and its mask inverse etc.

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img4.PNG'>

## 05. convert-color-tutorial.py

- cvtColor() - converting from bgr to hsv, vice-versa etc.
- inRange() 

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img5.PNG'> | <img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img6.PNG'> | <img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img7.PNG'>

## 06. thresholding-tutorial.py

cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV - a lot more thresholding types

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img8.png'> 

## 07. adaptive-thresholding-tutorial.py

cv2.adaptiveThreshold() - How it uses binary thresholding as well to make thresholding more clear and abstract.

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img9.png'> 

## 08. ostu-thresholding-tutorial.py

cv2.THRESH_OTSU - Performs ostu thresholding

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img10.png'> 

## 09. transformations1-tutorial.py

Transformation could be resizing, plane wise transforming shifting image.

<b>cv2.warpAffine</b> - Simple shifting in x and y direction, <b>cv2.getAffineTransform</b> - Performing shifting in all direction i.e, x,y,z .

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img11.PNG'> 
<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img12.PNG'> 
<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img13.PNG'> 

## 11. smoothing-tutorial.py

Smoothing is for removing noise from image and making an image less pixelated.

cv2.blur, cv2.GaussianBlur, cv2.MedianBlur - some of the blurring techniques

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img14.png'>
<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img15.png'> 

## 12. morphological-1-tutorial.py

Morphological operations basic one - erosion and dilation

<b> Erosion</b> -: Removing pixels from image
<b> Dilation </b> -: Adding pixels to image, basically expand the image.

<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img16.png'>
<img src='https://github.com/ridhimagarg/opencv-tutorials/blob/master/images/readme/img17.png'> 







