""" 
Program name: line_transmogrify_1.py 
Objective: Sub-divide a complex line from one shape to another shape. 

Keywords: Path, shape, transmogrify, intermediate positions. 
============================================================================79 
Comments:  Transmogrify = To change thoroughly, as into a different shape or form. 
The intermediate positions are calculated by interploating transition positions 
along a path. 

Tested on: Python versions 2.6, 2.7, 3.2 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 

root = Tk() 
root.title('Transmogrify one line into another.') 
cw = 650                                      # canvas width. 
ch = 400                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#================================================================== 
# Morph Functions 
def interpolation_delta(number_of_steps, num_1, num_2): 
    """ Divide the numerical interval between two numbers, num_1 and num_2, 
        into an equal number of steps. 
        The interval is divided into N equally spaced differences, 
        where N = number_of_steps. 
    """ 
    delta = (num_2 - num_1)/float( number_of_steps) 
    return delta 

def line_deltas(number_of_steps, line_1, line_2): 
    """ Lines, are passed as arguments in the form of 2D coordinate lists. 
        A list of the deltas for each sucessive pair of points is calculated. 
        The straight line joining each pair of corresponding points is divided 
        into equally spaced differences       
    """ 
    line_delta = [] 
    for i in range(len(line_1)): 
        new_value = interpolation_delta(number_of_steps, line_1[i], line_2[i]) 
        line_delta.append(new_value) 
    return line_delta 

# Test data and execution. 
#========================== 
line_1 = [0,200,   100,100,  200,50,  300,140,  400,180 ] 
line_2 = [450,10,  550,40,   570,70,  530,100,  490,340 ] 

number_of_steps = 20         # Number of transition steps in the morph process. 
radius1 = 8 
radius2 = 4 
# Convenient display position. 
x_shift, y_shift = 50, 50 
x_scale, y_scale = 1., 1. 

# Draw the Start and End lines 
''' The x-component and the y-component are dealt with separately because 
        we want to be able to scale and shift the horizontal components independently 
        fromthe vertical components. 
''' 
xy_start = [] 
xy_end   = [] 
for i in range(0, len(line_1), 2): 
    xx0   = line_1[i]  * x_scale + x_shift 
    yy0   = line_1[i+1]* y_scale + y_shift 
    xx1   = line_2[i]  * x_scale + x_shift 
    yy1   = line_2[i+1]* y_scale + y_shift 
    xy_start.append(xx0) 
    xy_start.append(yy0) 
    xy_end.append(xx1) 
    xy_end.append(yy1) 
canvas_1.create_line(xy_start, width=3, fill='blue') 
canvas_1.create_line(xy_end, width=3, fill='red') 

line_delta = line_deltas(number_of_steps, line_1, line_2) 

xy_intermediate = [] 
for j in range(number_of_steps): 
    for i in range(0, len(line_1), 2): 
        xx0 = (line_1[i]   + j * line_delta[i])   * x_scale + x_shift 
        yy0 = (line_1[i+1] + j * line_delta[i+1]) * y_scale + y_shift 
        xy_intermediate.append(xx0) 
        xy_intermediate.append(yy0) 
        canvas_1.create_oval(xx0-radius2, yy0+radius2, xx0+radius2, yy0-radius2, width=1, outline='green') 
    canvas_1.create_line(xy_intermediate, width=1, fill='green') 
    xy_intermediate = [] 

root.mainloop()
