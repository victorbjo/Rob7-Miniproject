import cv2
from cv2 import imshow
import numpy as np
def pixiExt ( img , x0 , y0 , radius):
    distCenter = []
    n1 = n2 = n = 0
    p1 = p2 = pm = 0
    i = []
    for y in range ( len ( img )):
        distCenter.append([])
        for x in range ( len ( img [ y ])):
            #if pixel is within radius of (x0, y0)
            dist_from_center = np.sqrt (( x0 - x ) ** 2 + ( y0 - y ) ** 2 )
            mask0 = dist_from_center <= radius
            mask1 = dist_from_center <= radius*1.25
            difference = not mask0 and mask1
            distCenter[-1].append(float(difference))
            n1 += mask0 #This is the amount of pixels in the inner most circle
            n += mask1 #This is the amount of pixels in the union of the two circles
            if mask0:
                p1 += img [ y ][ x ] #This is the inner most circle
            if mask1:
                pm += img [ y ][ x ] #This is the union of the two circles
                i.append(img [ y ][ x ]) #This is the intensity of the pixels in the union of the two circles
    n2 = n - n1 #This is the outer most circle
    pm = pm / n #Average intensity of the union of the two circles
    p2 = pm - p1 #Intensity of the outer most circle
    p2 = p2 / n2 #Average intensity of the outer most circle
    p1 = p1 / n1 #Average intensity of the inner most circle
    return n, n1, n2, p1, p2, pm, i

def SepFil(n,n1,n2,p1,p2,pm,i):
    x = 0
    A = 0
    for x in range(n):
        A  += (i[x]-pm)**2
    B = (n1 * (p1 - pm)**2) + (n2 * (p2 - pm)**2)

    WeirdN = B/A
    return WeirdN



coconut = cv2.imread('Coconuts\coconut.png')
mask = pixiExt(coconut, 100, 100, 50)
mask = np.array(mask)
cv2.imshow('mask', mask)
cv2.waitKey()
