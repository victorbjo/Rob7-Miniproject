import cv2
import numpy as np
from matplotlib import pyplot as plt
import Preprocessing
img = cv2.imread('Coconuts\coconut.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
width = 320
height = 240


img1 = Preprocessing.preprocessing(img)

#plt.imshow(img1, cmap = 'gray')

R = 50
bordersize = R
img_bordered = cv2.copyMakeBorder(
    img1,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[0]
)

# fig, ax = plt.subplots(1,2)
# ax[0].imshow(img1, cmap = 'gray')
# ax[0].set_title("original")
# ax[1].imshow(img_bordered, cmap = 'gray')
# ax[1].set_title("after padding")


img_blank = np.zeros( img_bordered.shape) 
#img_blank =  cv2.cvtColor(img_blank, cv2.COLOR_GRAY2BGR)
#[2*R+height, 2*R+width]
#plt.imshow( img_blank, cmap = 'gray')


for i in range(R:R+height):
    for j in range(R:R+width):
        if img_bordered[i,j]>200:
            


