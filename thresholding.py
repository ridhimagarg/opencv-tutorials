import cv2


img = cv2.imread('images/image8.jpg')

ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

images = [thresh1, thresh2, thresh3, thresh4, thresh5]
titles = ['Binary', 'Binary inverse', 'Truncate', 'Tozero', 'Tozero inverse']

for i in range(5):
    cv2.imshow(titles[i], images[i])
    cv2.waitKey(0)
)

