import cv2

img = cv2.imread('Coconuts\circles.png')
cv2.circle(img, (200,0), 35, (255,255,255))
cv2.circle(img, (200,0), 40, (255,255,255))
cv2.circle(img, (240,0), 35, (255,255,255))
cv2.circle(img, (120,40), 30, (255,255,255))
cv2.circle(img, (160,40), 40, (255,255,255))
cv2.circle(img, (200,40), 10, (255,255,255))


cv2.imshow('a',img)
cv2.waitKey()