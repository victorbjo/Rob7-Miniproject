import numpy.matlib
import numpy as np
import pandas
import matplotlib.pyplot as plt
import cv2
RR = 50
def distance_list(size, pos):
    pos_list = np.arange(size)

    # distance calculation of all matrix elements to the center of the circle
    diff_list = np.power(pos_list - pos, 2)
    return diff_list

   
def circleDrawing( x0, y0, r, width = 320, height = 240):
    # creating dummy metrices to calculate distance to the center
    row = np.arange(height)
    column = np.arange(width)

    # distance calculation of all matrix elements to the center of the circle
    diff_row = distance_list(height, y0)
    diff_column = distance_list(width, x0)
    row_m = np.matlib.repmat(diff_row, width, 1)
    column_m = np.matlib.repmat(diff_column, height, 1)
    # column_m = np.transpose(column_m)
    row_m = np.transpose(row_m)

    # drawing the circle
    dist = np.power(row_m + column_m, 0.5)
    df = pandas.DataFrame(dist)
    mask1 = pandas.DataFrame(np.zeros((height, width)))
    threshold = 2.5
    mask1[df > (r - threshold)] = 1
    mask2 = pandas.DataFrame(np.zeros((height, width)))
    mask2[df < (r + threshold)] = 1
    
    mask = mask1 + mask2
    mask[mask != 2] = 0
    mask[mask == 2] = 1

    array = pandas.DataFrame.to_numpy(mask)
    # bordersize = RR
    # array_padded = cv2.copyMakeBorder(
    # array,
    # top=bordersize,
    # bottom=bordersize,
    # left=bordersize,
    # right=bordersize,
    # borderType=cv2.BORDER_CONSTANT,
    # value=[0])


    return array

# plt.imshow(array)