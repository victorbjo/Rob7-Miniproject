import cv2
from cv2 import HoughCircles
import numpy as np
import SepFilter
def main(path): #Pretty much pseudo code
    picture = cv2.imread(path)
    #picture = preprocess()
    width = len(picture[0])
    height = len(picture)
    #Run function x for every 20 pixel
    for y in range(0, height, 20):
        for x in range(0, width, 20):
            if sepFilter(picture) < 0.1:
                results.append[HoughCircles(picture)]
if __name__ == "__main__":
    main('Coconuts\coconut1.png')

'''
TODO: We need to fix preprocessing, and make it easilier callable
We need to fix SepFilter to be actually callable, and make sure no code runs on init
We need to make sure that HoughCircles is actually callable. Not sure about .ipynb??? But iDunno
'''