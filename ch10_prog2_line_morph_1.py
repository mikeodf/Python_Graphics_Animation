""" 
Program name: line_morph_1.py 
Objective: Sub-divide the straight line path between two points into a specified 
number of equi-spaced steps. 

Keywords: Path,poit, intermediate positions, motion. 
============================================================================79 
Comments:  The lines are expressed as two x and y lists of coordinates. 
The intermediate positions are calculated by interploating transition positions 
along a path. 

Tested on: Python versions 2.6, 2.7, 3.2 
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python 3.2.3 and higher. 

root = Tk() 
root.title('Morph many points.') 
cw = 800                                      # canvas width. 
ch = 600                                      # canvas height. 
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
    return [ x_delta, y_delta ] 

def line_deltas(number_of_steps, line_1, line_2): 
    """ Lines, are passed as arguments in the form of 2D coordinate lists. 
        A list of the deltas for each sucessive pair of points is calculated. 
        The straight line joining each pair of corresponding points is divided into equally spaced differences       
    """ 
    line_delta = [] 
    for i in range(0,len(line_1)/2, 2): 
        x_delta = points_delta( number_of_steps, line_1[i], line_2[i]) 
        y_delta = points_delta( number_of_steps, line_1[i+1], line_2[i+1]) 
        line_delta.append(x_delta) 
        line_delta.append(y_delta) 
    return line_delta 
  
#=========================================================== 
xy0 = [ 10,60,  10,100,    10,140,    10,180,   10,220,   10,260,    10,300 ] 
xy1 = [700,0,  400,80,   700,160,   500,240,  700,450,  300,450,   100,450 ] 

number_of_steps = 30         # The number of transition steps in the morph process. 

radius1 = 8 
radius2 = 4 

# A convenient display position. 
x_shift, y_shift = 50, 50 
x_scale, y_scale = 1., 1. 

# Draw the Start and End points 
for i in range(0, len(xy0), 2): 
    xx0   = xy0[i]  * x_scale + x_shift 
    yy0 = xy0[i+1]* y_scale + y_shift 
    xx1   = xy1[i]  * x_scale + x_shift 
    yy1 = xy1[i+1]* y_scale + y_shift 
    canvas_1.create_oval(xx0- radius1, yy0 + radius1, xx0 + radius1, yy0 - radius1, width=3, outline='blue') 
    canvas_1.create_oval(xx1- radius1, yy1 + radius1, xx1 + radius1, yy1 - radius1, width=3, outline='red') 


for j in range(0, len(xy0), 2): 
    xya_line = [xy0[j], xy0[j+1] ]  # Express points as a list for later programming convenience. 
    xyb_line = [xy1[j], xy1[j+1] ] 
    point_delta = points_delta(number_of_steps, xya_line, xyb_line) 

    for i in range(1,number_of_steps+1): 
        xx0 = (xya_line[0] + i*point_delta[0]) * x_scale + x_shift 
        yy0 = (xya_line[1] + i*point_delta[1]) * y_scale + y_shift 
        canvas_1.create_oval(xx0-radius2, yy0+radius2, xx0+radius2, yy0-radius2, width=2, outline='green') 

root.mainloop()
