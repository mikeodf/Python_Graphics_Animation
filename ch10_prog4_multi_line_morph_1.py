"""
Program name: multi_line_morph_1.py
Objective: Sub-divide the straight line path between two lines into a specified 
number of equi-spaced steps.

Keywords: Path, point, line, intermediate positions, motion.
============================================================================79
Comments:  Transmogrify = To change thoroughly, as into a different shape or form.
or transform in a surprising or magical manner, a mid 17th century word.
The lines are expressed as two x and y lists of coordinates.
The intermediate positions are calculated by interploating transition positions
along a path.

Tested on: Python versions 2.6, 2.7, 3.2
Author:          Mike Ohlson de Fine
"""
#from Tkinter import *
from tkinter import *  # For Python 3.2.3 and higher.
import itertools

root = Tk()
root.title('Morph one line towards another.')
cw = 1200                                      # canvas width.
ch = 1200                                      # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0, column=1)
#==================================================================
# Morph Functions
def points_delta(number_of_steps, point_1, point_2):
    """ 2D points, point_1 =  (x1,y1) and point_2 =  (x2,y2) are passed as arguments
        and the straight line joining them is divided into N equally spaced differences,
        where N = number_of_steps.
    """
    x_delta = (point_2[0] - point_1[0])/float( number_of_steps) 
    y_delta = (point_2[1] - point_1[1])/float( number_of_steps) 
    return [x_delta, y_delta]

def line_deltas(number_of_steps, line_1, line_2):
    """ Lines, are passed as arguments in the form of 2D coordinate lists.
        A list of the deltas for each sucessive pair of points is calculated.
        The straight line joining each pair of corresponding points is divided into equally spaced differences       
    """
    line_delta = []
    for i in range(0,len(line_1),2):
        xy_sub0 = [line_1[i], line_1[i+1]]
        xy_sub1 = [line_2[i], line_2[i+1]]
        xy_del = points_delta( number_of_steps, xy_sub0,  xy_sub1) 
        line_delta.append(xy_del)
    # Flatten the resulting two dimensional list array.
    flatten = itertools.chain.from_iterable(line_delta)
    flat_line_delta = list(flatten)
    return flat_line_delta

# Test data and execution.
#==========================
xy_disk =  [[125.4, 62.49, 124.1, 53.12, 124.6, 45.65, 128.8, 37.23, 135.1, 31.24, 145.4, 27.74, 158.3, 28.98, 166.8, 35.39, 171.5, 42.15, 174.3, 50.03, 173.8, 58.1, 170.7, 65.75, 166.4, 71.92, 159.4, 76.42, 149.1, 78.32, 139.5, 77.07, 131.6, 72.09, 126.7, 65.57], [209.6, 156.6, 218.9, 160.3, 229.1, 160.9, 239.6, 156.0, 246.7, 147.2, 248.7, 137.8, 248.2, 128.8, 244.9, 120.9, 238.7, 113.9, 229.3, 109.8, 218.9, 109.6, 209.0, 113.7, 202.6, 121.5, 199.4, 130.7, 199.1, 141.2, 202.8, 149.0, 207.2, 154.3], [164.1, 203.9, 173.2, 201.8, 182.6, 203.9, 190.5, 208.5, 195.4, 215.4, 198.0, 223.5, 198.2, 233.2, 194.7, 241.6, 189.1, 248.6, 181.3, 252.6, 173.9, 254.1, 164.9, 252.0, 157.7, 248.0, 152.0, 241.7, 148.4, 233.7, 148.2, 225.1, 150.2, 218.7, 153.5, 211.7, 158.5, 206.7], [71.47, 186.1, 62.01, 185.9, 52.88, 190.2, 47.12, 197.1, 43.7, 204.9, 42.38, 213.7, 44.54, 222.2, 49.58, 229.5, 55.58, 234.8, 64.21, 237.0, 73.15, 237.2, 83.51, 231.8, 89.62, 224.6, 92.79, 215.8, 92.24, 207.0, 90.15, 199.2, 85.95, 192.9, 77.45, 187.6], [65.07, 114.2, 58.0, 119.9, 48.84, 123.9, 38.99, 123.0, 31.67, 119.6, 25.67, 113.5, 20.15, 104.8, 19.97, 95.84, 22.67, 85.04, 28.19, 77.78, 36.89, 73.34, 47.42, 72.32, 56.19, 74.3, 63.08, 79.88, 68.77, 87.02, 70.33, 96.32, 69.97, 103.8, 66.8, 110.5], [138.3, 119.8, 126.0, 117.7, 113.9, 121.4, 104.4, 131.7, 102.0, 146.8, 105.8, 157.1, 112.7, 164.9, 124.0, 169.6, 137.8, 166.7, 148.7, 156.7, 152.7, 144.7, 149.9, 132.4, 143.3, 123.3], [164.7, 131.6, 173.2, 133.2, 183.2, 130.1, 189.9, 125.7, 196.0, 115.4, 197.6, 103.0, 193.2, 93.04, 185.7, 84.76, 175.6, 81.7, 167.2, 81.7, 159.0, 84.94, 150.9, 92.38, 147.3, 103.7, 148.5, 116.0, 153.2, 123.9, 160.0, 130.1], [156.8, 158.3, 162.8, 151.8, 171.5, 147.2, 180.8, 146.6, 190.1, 150.0, 196.0, 154.8, 200.4, 162.9, 202.8, 170.7, 201.6, 179.0, 198.7, 187.5, 192.7, 193.5, 184.5, 197.7, 176.6, 198.3, 167.9, 196.6, 161.2, 192.6, 156.2, 186.8, 152.6, 177.9, 152.2, 169.5, 154.6, 162.2], [123.9, 175.4, 115.0, 176.5, 104.6, 183.1, 99.2, 192.4, 97.52, 202.9, 101.8, 215.1, 109.9, 223.9, 120.5, 227.3, 129.5, 227.1, 136.6, 223.7, 142.6, 218.2, 147.8, 208.0, 148.1, 198.6, 144.9, 188.9, 138.7, 180.9, 130.0, 176.6], [95.98, 148.5, 91.6, 139.1, 86.08, 132.6, 77.68, 128.3, 67.54, 128.2, 57.4, 131.7, 50.32, 139.6, 46.0, 150.3, 46.78, 161.9, 52.54, 171.9, 61.54, 177.7, 72.1, 180.1, 80.68, 178.0, 88.06, 172.8, 94.6, 164.5, 96.22, 153.0], [123.7, 103.4, 126.6, 95.48, 127.2, 86.84, 124.2, 77.48, 119.0, 70.4, 110.3, 65.31, 98.08, 64.3, 88.6, 68.61, 81.22, 75.98, 77.56, 87.5, 79.18, 100.3, 85.78, 110.2, 94.6, 114.9, 106.6, 115.9, 114.7, 112.8, 120.9, 106.9]]

xy_leaf = [[103.3, 130.1, 102.5, 122.8, 107.8, 109.7, 112.4, 99.5, 111.0, 94.9, 119.1, 96.4, 136.7, 96.0, 150.8, 99.9, 157.7, 111.8, 160.8, 122.1, 159.0, 130.7, 157.8, 144.6, 152.7, 142.5, 143.9, 143.7, 138.3, 149.4, 132.2, 138.8, 121.5, 129.9, 106.9, 129.9], 
[176.5, 164.1, 187.0, 162.9, 199.0, 165.0, 213.1, 161.8, 219.0, 152.0, 219.8, 135.8, 219.0, 122.8, 212.4, 120.6, 198.6, 114.0, 184.9, 110.1, 174.0, 112.2, 166.6, 123.1, 162.4, 133.0, 161.0, 144.0, 169.9, 149.5, 173.6, 156.5, 175.0, 160.8], 
[176.9, 167.9, 181.5, 167.4, 185.3, 171.3, 200.4, 171.7, 214.1, 175.2, 221.9, 186.1, 224.7, 202.3, 222.9, 216.8, 225.0, 225.9, 219.4, 223.8, 203.6, 222.7, 183.1, 223.8, 168.7, 219.6, 161.3, 208.0, 160.3, 195.3, 157.4, 183.3, 156.7, 179.2, 165.7, 176.0, 173.6, 171.1], 
[137.4, 171.7, 132.6, 177.3, 124.3, 182.6, 113.8, 186.1, 105.0, 193.2, 101.8, 202.3, 106.4, 212.5, 109.9, 222.7, 115.9, 220.6, 126.8, 220.3, 140.2, 223.1, 151.5, 222.4, 156.7, 211.5, 156.0, 196.8, 153.6, 186.1, 153.6, 180.2, 146.6, 177.1, 141.4, 172.7], 
[136.9, 168.0, 131.6, 172.5, 122.8, 179.1, 108.9, 182.6, 93.7, 183.0, 83.14, 174.2, 76.45, 160.8, 73.63, 152.3, 67.29, 148.8, 78.91, 145.6, 89.47, 139.7, 102.5, 134.0, 119.1, 133.3, 128.6, 139.7, 134.6, 148.1, 136.7, 153.1, 135.1, 158.5, 136.3, 165.4], 
[157.9, 147.6, 151.9, 145.9, 145.0, 147.5, 140.6, 152.6, 138.9, 159.5, 141.5, 167.6, 146.2, 172.1, 154.1, 175.3, 164.1, 172.7, 170.4, 168.0, 171.4, 160.4, 168.1, 152.5, 161.3, 148.5], 
[89.81, 112.2, 101.1, 103.0, 99.71, 87.54, 91.61, 76.94, 76.41, 70.64, 62.41, 67.13, 47.61, 68.94, 36.31, 70.64, 22.51, 68.94, 27.81, 81.24, 33.51, 93.14, 38.11, 107.2, 48.31, 118.5, 64.81, 125.5, 79.31, 123.8, 87.71, 114.6], 
[237.7, 153.2, 237.3, 141.5, 246.4, 135.3, 259.3, 139.2, 272.4, 147.0, 281.7, 155.4, 290.0, 166.4, 298.0, 179.9, 300.5, 191.3, 306.0, 197.4, 293.5, 197.1, 280.4, 194.1, 270.2, 194.2, 257.8, 195.7, 243.0, 191.0, 230.7, 179.8, 228.7, 166.6, 230.6, 158.1, 235.5, 155.3], 
[164.7, 92.69, 174.8, 95.41, 189.0, 91.8, 199.1, 83.52, 205.4, 69.26, 208.0, 54.99, 203.7, 39.42, 195.6, 28.65, 181.8, 15.09, 179.7, 29.48, 169.1, 39.38, 157.6, 49.3, 144.6, 62.16, 141.2, 76.26, 148.5, 87.84, 161.2, 91.14],
[156.1, 233.9, 145.7, 235.3, 133.9, 244.3, 127.9, 255.8, 127.6, 271.3, 130.7, 285.6, 140.7, 298.2, 152.4, 305.0, 170.4, 312.1, 166.8, 298.0, 172.7, 284.8, 179.5, 271.2, 186.4, 254.2, 184.1, 239.9, 172.8, 232.1, 159.8, 234.0],
[92.28, 206.6, 87.0, 197.5, 74.32, 190.1, 61.3, 189.0, 46.86, 194.7, 34.92, 203.1, 27.12, 217.2, 25.42, 230.6, 25.72, 249.9, 37.32, 241.1, 51.79, 241.5, 66.93, 242.5, 85.24, 242.5, 97.51, 234.8, 100.4, 221.4, 93.69, 210.1]]
'''
# Verify that the line-shapes in each set match in length.
print 'len(xy_disk): ' ,len(xy_disk)
print 'len(xy_leaf): ' ,len(xy_leaf)

for i in range(len(xy_disk)):
    print 'len(xy_disk[i]): ' ,len(xy_disk[i])
    print 'len(xy_leaf[i]): ' ,len(xy_leaf[i])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
'''

xy0 = xy_disk
xy1 = xy_leaf
number_of_steps = 8         # Number of transition steps in the morph process.
radius1 = 4
radius2 = 2
# Convenient display position.
x_shift, y_shift = 200, 0
x_scale, y_scale = 3., 3.

# Draw the Start and End lines
xy_start = []
xy_end   = []
for k in range(len(xy_disk)):
    for i in range(0, len(xy_disk[k]), 2):
        xx0   = xy0[k][i]  * x_scale + x_shift
        yy0   = xy0[k][i+1]* y_scale + y_shift
        xx1   = xy1[k][i]  * x_scale + x_shift
        yy1   = xy1[k][i+1]* y_scale + y_shift
        xy_start.append(xx0)
        xy_start.append(yy0)
        xy_end.append(xx1)
        xy_end.append(yy1)
    canvas_1.create_line(xy_start, width=5, fill='blue')
    canvas_1.create_line(xy_end, width=5, fill='red')
    xy_start = []
    xy_end   = []


# Draw the intermediate lines.
xy_intermediate = []
xy_line_deltas = []
delta_j = []

for k in range(len(xy0)):
    print ('len(xy0): ' ,len(xy0))
    del_j = line_deltas(number_of_steps, xy0[k], xy1[k])
    delta_j.append(del_j)

for k in range(len(xy0)):

    for j in range(number_of_steps):
        for i in range(0, len(xy0[k]), 2):
            xx0 = (xy0[k][i]   + j * delta_j[k][i])   * x_scale + x_shift
            yy0 = (xy0[k][i+1] + j * delta_j[k][i+1]) * y_scale + y_shift 
            xy_intermediate.append(xx0)
            xy_intermediate.append(yy0)
            canvas_1.create_oval(xx0-radius2, yy0+radius2, xx0+radius2, yy0-radius2, width=1, outline='green')
        canvas_1.create_line(xy_intermediate, width=1, fill='green')
        xy_intermediate = []

root.mainloop()
