""" 
Program name: point_morph_1.py 
Objective: Sub-divide the straight line path between two points into a specified 
number of equi-spaced steps. 

Keywords: Path, point, intermediate positions. 
============================================================================79 
Comments:  The intermediate positions are calculated by interploating 
transition positions along a path. 
The code here is easily adapted to lines which are lists of many x and y coordinates. 

Tested on: Python versions 2.6, 2.7, 3.2 
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python 3.2.3 and higher. 

root = Tk() 
root.title('Morph one point towards another.') 
cw = 800                                      # canvas width. 
ch = 200                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#================================================================ 
# The Fundamental Morph Functions. 
def points_delta(number_of_steps, point_1, point_2): 
    """ 2D points, point_1 =  (x0,y0) and point_2 =  (x1,y1) are passed as arguments 
        and the straight line joining them is divided into N equally spaced differences, 
        where N = number_of_steps. The result returned are the incremental differences, 
        also known as 'deltas'. 
    """ 
    x_delta = (point_2[0] - point_1[0])/float( number_of_steps) 
    y_delta = (point_2[1] - point_1[1])/float( number_of_steps) 
    return [ x_delta, y_delta ] 

#=========================================================== 
xy0 = [ 10,60 ]    # Start position. 
xy1 = [700,0  ]    # End position. 

number_of_steps = 30         # Number of transition steps in the morph process. 

radius1 = 10    # Radius of start and end markers. 
radius2 = 4      # Radius of intermediate position markers. 

# Convenient display position. 
x_shift, y_shift = 50, 50 
x_scale, y_scale = 1., 1. 

# Draw the Start and End points at a convenient viewing positions on the canvas. 
for i in range(0, len(xy0), 2): 
    xx0   = xy0[i]  * x_scale + x_shift 
    yy0 = xy0[i+1]* y_scale + y_shift 
    xx1   = xy1[i]  * x_scale + x_shift 
    yy1 = xy1[i+1]* y_scale + y_shift 
    canvas_1.create_oval(xx0- radius1, yy0 + radius1, xx0 + radius1, yy0 - radius1, width=6, outline='blue') 
    canvas_1.create_oval(xx1- radius1, yy1 + radius1, xx1 + radius1, yy1 - radius1, width=6, outline='red') 

point_delta = points_delta(number_of_steps, xy0, xy1) 

for i in range(1,number_of_steps+1): 
    xx0 = (xy0[0] + i*point_delta[0]) * x_scale + x_shift 
    yy0 = (xy0[1] + i*point_delta[1]) * y_scale + y_shift 
    canvas_1.create_oval(xx0-radius2, yy0+radius2, xx0+radius2, yy0-radius2, width=4, outline='green') 

root.mainloop()
