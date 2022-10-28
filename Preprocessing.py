import cv2
import numpy as np
 
def preprocessing(img): 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Cropping an image
    cropped_image = gray[80:200, 0:240]
    width = 320
    height = 240
    points = (width, height)
    resized = cv2.resize(cropped_image, points, interpolation= cv2.INTER_LINEAR)

    return resized



coconut = cv2.imread('Coconuts\coconut.png')
coconut1 = cv2.imread('Coconuts\coconut1.png')
coconut2 = cv2.imread('Coconuts\coconut2.png')

#cv2.imshow('asd', coconut1)
#cv2.waitKey()
coconutRe = preprocessing(coconut)
coconutRe1 = preprocessing(coconut1)
coconutRe2 = preprocessing(coconut2)

cv2.imshow('original image', coconut)
cv2.imshow('resized image', coconutRe)
cv2.imshow('resized1 image', coconutRe1)
cv2.imshow('resized2 image', coconutRe2)
cv2.waitKey()
