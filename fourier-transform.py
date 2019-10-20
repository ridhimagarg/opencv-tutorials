import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/messi.jpg', 0)

# print(img.shape)

# cv2.imshow('image',img)

f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')

plt.show()