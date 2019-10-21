import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/mario.jpg',0 )
template = cv2.imread('images/mario_coin.jpg', 0)

print(img.shape)
print(template.shape)
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
thresh =0.8

print(res)