import cv2

print(dir(cv2))

print([i for i in dir(cv2) if 'EVENT' in i])

## Initializing the coordinates for image to crop
start_x = 0
start_y = 0
end_x = 0
end_y = 0

## Defining the mouse callbacks to be called accordingly
def crop_image(event,x,y,flags,param):
    global start_x, start_y, end_x, end_y

    ## If leftbuttondowm then fetch coordinates that will be starting coordinates 
    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y

    ## If leftbuttonup then fetch coordinates that will be ending coordinates 
    if event == cv2.EVENT_LBUTTONUP:
        end_x, end_y = x, y


image = cv2.imread('images/image8.jpg')
## creating a window
cv2.namedWindow('Cropping')
## setting callback on that window
cv2.setMouseCallback('Cropping', crop_image)

## Cropping main loop
while(1):
    cv2.imshow('Cropping',image)
    if cv2.waitKey(0) :
        new_img = image[start_y:end_y, start_x:end_x]
        cv2.imshow('Cropped',new_img)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()




