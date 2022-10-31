
import cv2
import numpy as np
from matplotlib import pyplot as plt
import Preprocessing
from circle import circleDrawing
import SepFilter as sp
import pandas as pd

width = 320
height = 240
R = 50
rr = 23
img = cv2.imread('Coconuts\coconut.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# dim = (width, height)
# new_img = cv2.resize(img, dim)
#cv2.imshow('graycsale image',img)
#plt.imshow(new_img, cmap = 'gray')

img1 = Preprocessing.preprocessing(img)

plt.imshow(img1, cmap = 'gray')

# img2 = sp.sepFil(img1,)


# bordersize = R
# img_bordered = cv2.copyMakeBorder(
#     img1,
#     top=bordersize,
#     bottom=bordersize,
#     left=bordersize,
#     right=bordersize,
#     borderType=cv2.BORDER_CONSTANT,
#     value=[0]
# )



# fig, ax = plt.subplots(1,2)
# ax[0].imshow(img1, cmap = 'gray')
# ax[0].set_title("original")
# ax[1].imshow(img_bordered, cmap = 'gray')
# ax[1].set_title("after padding")


# cv2.imshow('picture prepocessed',border)
# cv2.waitKey()


#img_blank = np.zeros( img_bordered.shape) 
#img_blank =  cv2.cvtColor(img_blank, cv2.COLOR_GRAY2BGR)
#[2*R+height, 2*R+width]
#plt.imshow( img_blank, cmap = 'gray')
img_blank = np.zeros( img1.shape) 
img_blank.shape


# plt.imshow(circleDrawing(  10, 10, 10, width, height), cmap='gray')
#plt.imshow(img_blank, cmap='gray')

a_test = circleDrawing(50,100,20,width,height)
a_test = a_test + img_blank
plt.imshow(a_test, cmap='gray')
a_test.shape



for i in range(0, height):
    for j in range(0, width):
        if a_test[i,j]>0:
            img_blank = img_blank + circleDrawing(  i, j, rr, width, height)     


# ********** with padding
#  rr = 23
# for i in range(R, R+height):
#     for j in range(R, R+width):
#         if a_test[i,j]>0:
#             img_blank = img_blank + circleDrawing(  i, j, rr, width, height)            


plt.imshow(img_blank,cmap='gray')
# print(img_blank[50:100,50:100])


plt.hist(img_blank.ravel(),256,[0,256]); plt.show()


new_img = img_blank[img_blank>10]
plt.imshow(new_img,cmap='gray')
# cv2.imwrite("circled.png",new_img)



# 
