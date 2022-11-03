import cv2
# from cv2 import HoughCircles
import numpy as np
import SepFilter
import HoughCircle as HC
import Preprocessing as pp
import matplotlib.pyplot as plt

def main(path): #Pretty much pseudo code
    np.seterr(divide='ignore', invalid='ignore')
    picture = cv2.imread(path)
    cv2.imshow('a', picture)
    cv2.waitKey()
    picture = pp.preprocessing(picture)
    print("preprocessing done!")
    width = len(picture[0])
    height = len(picture)

    #Run function x for every 20 pixel
    for y in range(0, height, 40):
        print("current y")
        print(y)
        for x in range(0, width, 40):
            sepFilterResults = SepFilter.sepFil(picture, x, y)
            hough_circle_dataframe = HC.initial_hough_Dataframe()
            for idx, result in enumerate(sepFilterResults):
                if result >= 0.05:
                    r = idx*10+10
                    isCircle, circled_object, hough_score, mean_x, mean_y = HC.HoughCircles(picture, x, y, r)
                    new_row = [isCircle, circled_object, hough_score, mean_x, mean_y]
                    HC.append_hough_row(hough_circle_dataframe, new_row)
                    print("new possible circle!")
                    print(isCircle)
                    print(result)
                    print(idx)
                    print("y ")
                    print(y)
                    print(mean_y)
                    print("x")
                    print(x)
                    print(mean_x)
                    print("hough score")
                    print(hough_score)
                    # plt.imshow(circled_object)
                    if isCircle == 1 :
                        print("circle detected!")   
                        cv2.imshow('possible circle',circled_object)
                        cv2.waitKey()

            
            # print(hough_circle_dataframe[hough_circle_dataframe['IS CIRCLE']])
        

    cv2.imshow('a', picture)
    cv2.waitKey()

if __name__ == "__main__":
    main('Coconuts\coconutT.png')

'''
TODO: We need to fix preprocessing, and make it easilier callable
We need to fix SepFilter to be actually callable, and make sure no code runs on init
We need to make sure that HoughCircles is actually callable. Not sure about .ipynb??? But iDunno
'''