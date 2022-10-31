import numpy.matlib
import numpy as np
import pandas
import matplotlib.pyplot as plt
import cv2
RR = 50

def circleDrawing(width = 320, height = 240, x0, y0, r):
    # creating dummy metrices to calculate distance to the center
    row = np.arange(height)
    column = np.arange(width)
    row_m = np.matlib.repmat(row, width, 1)
    column_m = np.matlib.repmat(column, height, 1)
    column_m = np.transpose(column_m)

    # distance calculation of all matrix elements to the center of the circle
    diff_row = np.power(row_m - y0, 2)
    diff_colum = np.power(column_m - x0, 2)

    # drawing the circle
    dist = np.power(diff_row + diff_colum, 0.5)
    df = pandas.DataFrame(dist)
    mask1 = pandas.DataFrame(np.zeros((height, width)))
    threshold = 0.55
    mask1[df > (r - threshold)] = 1
    mask2 = pandas.DataFrame(np.zeros((height, width)))
    mask2[df < (r + threshold)] = 1
    
    mask = mask1 + mask2
    mask[mask != 2] = 0
    mask[mask == 2] = 1

    array = pandas.DataFrame.to_numpy(mask)
    bordersize = RR
    array_padded = cv2.copyMakeBorder(
    array,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[0]
)


    return array_padded

# plt.imshow(array)