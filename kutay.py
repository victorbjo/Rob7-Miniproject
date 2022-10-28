import numpy.matlib
import numpy
import pandas
from matplotlib.pyplot import imshow

r = 20
x0 = 200
y0 = 100

width = 320
height = 240
row = numpy.arange(height)
column = numpy.arange(width)

row_m = numpy.matlib.repmat(row, width, 1)
colum_m = numpy.matlib.repmat(column, height, 1)
colum_m = numpy.transpose(colum_m)

diff_row = numpy.power(row_m - y0, 2)
diff_colum = numpy.power(colum_m - x0, 2)

dist = numpy.power(diff_row + diff_colum, 0.5)
df = pandas.DataFrame(dist)
mask1 = pandas.DataFrame(numpy.zeros((240, 320)))
mask1[df > (r-0.55)] = 1
mask2 = pandas.DataFrame(numpy.zeros((240, 320)))
mask2[df < (r+0.55)] = 1
mask = mask1 + mask2
mask[mask != 2] = 0
mask[mask == 2] = 1
array = pandas.DataFrame.to_numpy(mask)

imshow(array)


# print(row_m)
# print(dist)