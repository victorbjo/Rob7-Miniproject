
import cv2
import numpy as np
from matplotlib import pyplot as plt
import Preprocessing
from circle import circleDrawing, distance_list
import SepFilter as sp
import pandas as pd

# width = 320
# height = 240

threshold_circle_check =  30

img = cv2.imread('Coconuts\coconut.png')

def HoughCircles(picture, window_i, window_j, rr):
    isCircle = 0
    height, width= picture.shape
    # img1 = Preprocessing.preprocessing(img) # already preprocessed
    img_blank = np.zeros( picture.shape)
    circled_object = img_blank
     
    # a_test = circleDrawing(290, 100, 35, width, height)
    # plt.imshow(a_test, cmap='gray')

    # for i in range(0, width):
    #     for j in range(0, height):
    #         if picture[j, i]>0:
    #             img_blank = img_blank + circleDrawing(  i, j, rr, width, height)     


    # window_i,j are inputs (top left of the window)
    for i in range(max(window_i - rr, 0), min(window_i + rr, width)):
        for j in range(max(window_j - rr, 0), min(window_j + rr, height)):
            if picture[j, i]>0:
                img_blank = img_blank + circleDrawing(i, j, rr, width, height)
    plt.imshow(img_blank,cmap='gray')
    number_mean = int(rr/4)
    img_blank_larg_ind = largest_indices(img_blank, number_mean) ###################### maybe change 2 * rr
    mean_x = int(img_blank_larg_ind[1].sum()/number_mean)
    mean_y = int(img_blank_larg_ind[0].sum()/number_mean)
    print("distance")
    print(np.power(np.power(np.abs(window_i + rr - mean_x),2)+np.power(np.abs(window_j + rr - mean_y),2),0.5))
    print("radius")
    print(rr)
    # print(mean_x)
    # print( mean_y)
    img_blank_larg_val = np.mean(img_blank[img_blank_larg_ind])
    if np.power(np.power(np.abs(window_i +rr - mean_x),2)+np.power(np.abs(window_j +rr - mean_y),2),0.5) < threshold_circle_check :
        # print('immmmmmmmmmmmm heeeeeeeeeeeeeeeeeeeere')
        isCircle = 1
        circled_object = picture + circleDrawing(mean_x, mean_y, rr, width, height)*200
    return isCircle, circled_object, img_blank_larg_val, mean_x, mean_y
        
        


def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)

# int(largest_indices(img_blank, 10)[0].sum()/10)
def append_hough_row(df, new_row):
    columns=['IS CIRCLE', 'CIRCLED IMG', 'HOUGH SCORE', 'MEAN X', ' MEAN Y']
    return pd.concat([ df, pd.DataFrame([new_row], columns=columns_name())], join = "inner")
def columns_name():
    return ['IS CIRCLE', 'CIRCLED IMG', 'HOUGH SCORE', 'MEAN X', ' MEAN Y']
def initial_hough_Dataframe():
    return pd.DataFrame([], columns= columns_name())