import numpy.matlib
import numpy as np
import pandas
import matplotlib.pyplot as plt
import cv2
RR = 50
def distance_list(height_size, width_size, pos_x, pos_y):
    height_list = np.arange(height_size)
    width_list = np.arange(width_size)

    # distance calculation of all matrix elements to the center of the circle
    y_diff_list = np.power(height_list - pos_y, 2)
    x_diff_list = np.power(width_list - pos_x, 2) 
    row_m = np.matlib.repmat(y_diff_list, width_size, 1)
    column_m = np.matlib.repmat(x_diff_list, height_size, 1)
    # column_m = np.transpose(column_m)
    row_m = np.transpose(row_m)

    # drawing the circle
    dist = np.power(row_m + column_m, 0.5) 
    return dist
# dist_list_row = distance_list(height, y0)
# dist_list_column = distance_list(width, x0)
   
def circleDrawing( x0, y0, r, width = 320, height = 240, dist1 = 0):
    # creating dummy metrices to calculate distance to the center
    # distance calculation of all matrix elements to the center of the circle
    # diff_x, diff_y = distance_list(height, width, x0, y0)

    # row_m = np.matlib.repmat(diff_y, width, 1)
    # column_m = np.matlib.repmat(diff_x, height, 1)
    # # column_m = np.transpose(column_m)
    # row_m = np.transpose(row_m)

    # # drawing the circle
    # dist = np.power(row_m + column_m, 0.5)
    dist = distance_list(height, width, x0, y0)
    df = pandas.DataFrame(dist)
    mask1 = pandas.DataFrame(np.zeros((height, width)))
    threshold = 0.6
    mask1[df > (r - threshold)] = 1
    mask2 = pandas.DataFrame(np.zeros((height, width)))
    mask2[df < (r + threshold)] = 1
    
    mask = mask1 + mask2
    mask[mask != 2] = 0
    mask[mask == 2] = 1

    array = pandas.DataFrame.to_numpy(mask)
    return array

# plt.imshow(array)