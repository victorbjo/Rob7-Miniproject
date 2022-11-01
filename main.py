import cv2
from cv2 import HoughCircles
import numpy as np
import SepFilter
import Preprocessing as pp
def main(path): #Pretty much pseudo code
    picture = cv2.imread(path)
    picture = pp.preprocessing(picture)
    width = len(picture[0])
    height = len(picture)

    #Run function x for every 20 pixel
    for y in range(0, height, 40):
        for x in range(0, width, 40):
            sepFilterResults = SepFilter.sepFil(picture, x, y)
            for idx, result in enumerate(sepFilterResults):
                if result >= 0.1:
                    r = idx*10+20
                    #HoughCircles(picture, r)
                    print(result)
                    print(idx)
                    print(y)
                    print(x)
                    print(result)
        print(y)
    cv2.imshow('a', picture)
    cv2.waitKey()

if __name__ == "__main__":
    main('Coconuts\test.png')

'''
TODO: We need to fix preprocessing, and make it easilier callable
We need to fix SepFilter to be actually callable, and make sure no code runs on init
We need to make sure that HoughCircles is actually callable. Not sure about .ipynb??? But iDunno
'''