import cv2
import numpy as np
 

def scale(img):
    preferredWidth = 320
    prefferedHeight = 240
    currentWidth = len(img[0])
    currentHeight = len(img)
    print("Current Width: ", currentWidth)
    print("Current Height: ", currentHeight)
    tempWidth = tempHeight = 0
    if currentWidth/currentHeight < preferredWidth/prefferedHeight:
        tempWidth = preferredWidth
        tempHeight = int(preferredWidth/currentWidth*currentHeight)
    else:
        tempHeight = prefferedHeight
        tempWidth = int(prefferedHeight/currentHeight*currentWidth)
    print(tempWidth, tempHeight)
    img = cv2.resize(img, (tempWidth, tempHeight))
    return img
def crop(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Cropping an image
    prefWidth = 320
    prefHeight = 240
    currentWidth = len(img[0])
    currentHeight = len(img)
    #crop it equally from all sides
    widthCrop = int((currentWidth - prefWidth)/2)
    heightCrop = int((currentHeight - prefHeight)/2)
    cropped_image = gray[heightCrop:currentHeight-heightCrop, widthCrop:currentWidth-widthCrop]
    return cropped_image

def preprocessing(img): 
    img = crop(scale(img))
    return img



coconut = cv2.imread('Coconuts\coconut2.png')
#coconut1 = cv2.imread('Coconuts\coconut1.png')
#coconut2 = cv2.imread('Coconuts\coconut2.png')

#cv2.imshow('asd', coconut1)
#cv2.waitKey()
coconutRe = preprocessing(coconut)
#coconutRe1 = preprocessing(coconut1)
#coconutRe2 = preprocessing(coconut2)

cv2.imshow('original image', coconut)
cv2.imshow('resized image', coconutRe)
#cv2.imshow('resized1 image', coconutRe1)
#cv2.imshow('resized2 image', coconutRe2)
cv2.waitKey()
