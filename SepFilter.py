import cv2
from cv2 import imshow
import numpy as np
def pixiExt ( img , x0 , y0 , radius):
    #loop through image img
    distCenter = []
    numPixels = 0
    for y in range ( len ( img )):
        distCenter.append([])
        for x in range ( len ( img [ y ])):
            #if pixel is within radius of (x0, y0)
            dist_from_center = np.sqrt (( x0 - x ) ** 2 + ( y0 - y ) ** 2 )
            mask0 = dist_from_center <= radius
            numPixels += mask0
            mask1 = dist_from_center <= radius*1.25
            distCenter[-1].append(float(not mask0 and mask1))

    #mask0 = dist_from_center <= radius
    #mask1 = dist_from_center <= radius *1.25
    #mask2 = mask1 & ~ mask0
    print(numPixels)
    return distCenter
value1 = False
value2 = False
print(value1 & ~ value2)
print(not value2 and value1)
coconut = cv2.imread('Coconuts\coconut.png')
mask = pixiExt(coconut, 100, 100, 50)
mask = np.array(mask)
cv2.imshow('mask', mask)
cv2.waitKey()
