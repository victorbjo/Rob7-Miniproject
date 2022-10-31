
import numpy as np 
import pandas
import matplotlib.pyplot as plt

r = 20
x0 = 200
y0 = 100

width = 320
height = 240
row = np.arange(height)
column = np.arange(width)

row_m = np.matlib.repmat(row, width, 1)
colum_m = np.matlib.repmat(column, height, 1)
colum_m = np.transpose(colum_m)

diff_row = np.power(row_m - y0, 2)
diff_colum = np.power(colum_m - x0, 2)

dist = np.power(diff_row + diff_colum, 0.5)
df = pandas.DataFrame(dist)
mask1 = pandas.DataFrame(np.zeros((240, 320)))
mask1[df > (r-0.55)] = 1
mask2 = pandas.DataFrame(np.zeros((240, 320)))
mask2[df < (r+0.55)] = 1
mask = mask1 + mask2
mask[mask != 2] = 0
mask[mask == 2] = 1
array = pandas.DataFrame.to_np(mask)

plt.imshow(array)


# print(row_m)
# print(dist)