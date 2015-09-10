"""
Program name: legs_walking_gait_modification_1.py
Objective: Animate a rudimentary walking stride with repeated steps.

Keywords: canvas, legs, walking, repeated stride stride
============================================================================79 
Comments: The hip, knee,and foot positions are were derived from Inkscape sketches.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
import math
import copy
import time
root = Tk()
root.title("Designer Walks: Varying stride length.") 

cw = 1300                                   # canvas width
ch = 150                                   # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 100 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    chart_1.delete('line_1')      # This erases everything on the canvas.
#======================================================================================================================
# Designer limb trajectories: Walks with limp.

hips = [ 140.9,120.7 , 157.1,119.2 , 174.5,109.9 , 190.9,103.8 , 210.4,100.3 , 224.3,99.03 , 238.6,102.6 , 250,110.9 , 265.7,116 , 282.1,116 , 296,108.4 , 313.9,100 , 330.3,92.46 , 349.3,87.41 , 365.2,91.2 , 379.6,104.6 , 394.2,115.4 , 416.7,118.2]

knee_a = [ 133.1,236.4 , 162.9,218.7 , 192.9,216 , 240.9,205.6 , 271.5,204.6 , 284.1,214.9 , 295.2,222.5 , 307.6,228.8 , 320.2,230.9 , 331.3,229.3 , 341.4,229.1 , 351.8,228.3 , 360.9,227.8 , 370.2,228.6 , 378.6,228.6 , 388.7,230.4 , 398.3,232.4 , 408.3,234.4]

knee_b = [ 182.8,237.4 , 193.9,237.9 , 204.6,236.9 , 212.9,236.9 , 222,236.7 , 231.6,237.2 , 240.7,238.7 , 250,240.5 , 258.9,243 , 271.2,244.2 , 292.4,231.1 , 315.9,215.2 , 336.4,203.8 , 366.2,197.8 , 396.7,205.3 , 421,220 , 437.6,224.5 , 456.9,232.9]

heel_a = [ 73.99,376.3 , 87.63,356.4 , 104.8,337.2 , 145.5,313.2 , 187.1,299.3 , 239.7,315.5 , 279.3,346.3 , 319.7,364.2 , 348,377.1
, 348,377.1, 348,377.1, 348,377.1 , 348,377.1, 348,377.1, 348,377.1 , 348,377.1, 348,377.1, 348,377.1 ]

heel_b = [ 210.4,374.8 ,210.4,374.8 ,210.4,374.8 , 210.4,374.8 ,210.4,374.8 ,210.4,374.8 , 210.4,374.8 ,210.4,374.8 ,210.4,374.8 ,
210.4,374.8 , 238.9,363.2 , 278,346 , 318.2,315 , 370.5,298.8 , 413.2,311.9 , 452.5,335.7 , 470.5,353.8 , 484.9,373.5]
#======================================================================================================================
shapes = [ hips, knee_a, knee_b, heel_a, heel_b ]
#======================================================================================================================


def scale_shape(shape, x_amp, y_amp, x_offset, y_offset):
    """ Amplify/attenuate and/or position a shape.
        First amplify then add the offset. That is, the offset is not amplified.
    """
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])

    # Amplify, add offsets and re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = ( x_list[j] * x_amp ) + x_offset 
        new_shape.append( x_list[j] )
        y_list[j] = ( y_list[j] * y_amp ) + y_offset 
        new_shape.append( y_list[j] ) 
    return new_shape
  
def draw_walker(indx, shapes):
    """ Draw entire body as a stick man.
    """
    # hips
    chart_1.create_oval(shapes[0][indx]-6, shapes[0][indx+1]-6,shapes[0][indx]+6, shapes[0][indx+1]+6, outline= "magenta", width = 1, tag = 'line_1') 
    # Hip to knee
    chart_1.create_line(shapes[0][indx], shapes[0][indx+1], shapes[1][indx], shapes[1][indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(shapes[0][indx], shapes[0][indx+1], shapes[2][indx], shapes[2][indx+1], fill= "green", width = 2, tag = 'line_1') 
    # knee to heel.    
    chart_1.create_line(shapes[1][indx], shapes[1][indx+1], shapes[3][indx], shapes[3][indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(shapes[2][indx], shapes[2][indx+1], shapes[4][indx], shapes[4][indx+1], fill= "green", width = 2, tag = 'line_1') 
    # feet.  
    chart_1.create_oval(shapes[3][indx]-3, shapes[3][indx+1]-4,shapes[3][indx]+20, shapes[3][indx+1]+4, fill= "blue", width = 1, tag = 'line_1') 
    chart_1.create_oval(shapes[4][indx]-3, shapes[4][indx+1]-4,shapes[4][indx]+20, shapes[4][indx+1]+4, fill= "green", width = 1, tag = 'line_1') 

def walk_1stride(shapes):
    """  Walk one stride.
    """
    for i in range(len(hips)/2):
        draw_walker(2*i, shapes)
        animdelay()

def scale_shape_group(shapes, x_amp, y_amp, x_offset, y_offset):
    """Perform scale_shape on each member of a shape set or group.
       Used to animate figures specified by trajectory.
    """
    for i in range(len(shapes)):
        shapes[i] = scale_shape(shapes[i], x_amp, y_amp, x_offset, y_offset)
    return shapes
#======================================================================
# Test and Demonstrate
''' NOTE: Whenever "scale_shape" is applied with offsets (ie x_offset or y_offset ) a permanent offset distortion 
is applied to the shape. This contminates amplification because any accumulated offsets will also be amplified.
This is why an unaltered version of the original shape must be preserved.
This re-enforces the argument for keeping normalized versions of important shapes.
''' 
shapes_1 = copy.deepcopy(shapes)   # Leave original undistorted.

# Phase 1
# shapes_1 is a currently sized (ie. amplified) version with no distorting offsets.
shapes_1 = scale_shape_group(shapes_1, 0.7, 0.3, 0.0, 0.0)
walk_1stride(shapes_1) # First stride
stride_len = shapes_1[3][len(shapes_1[3])-2]  - shapes_1[3][0]
#stride_start = shapes_1[3][0]
# Horizontal offset applied to accomodate next stride.
shapes_2 = scale_shape_group(shapes_1, 1.0, 1.0, stride_len, 0.0)
walk_1stride(shapes_2) #Second stride

# Phase 2
# Shorten stride length by x_amp = 0.7
stride_end = shapes_2[3][len(shapes_2[3])-2]
shapes_1 = copy.deepcopy(shapes) 
shapes_1 = scale_shape_group(shapes_1, 0.7*0.7, 0.3, 0.0, 0.0)
stride_len = shapes_1[3][len(shapes_1[3])-2]  - shapes_1[3][0]
# Horizontal offset applied to accomodate next stride asd well as continue from last step.
shapes_2 = scale_shape_group(shapes_1, 1.0, 1.0, stride_end , 0.0)
walk_1stride(shapes_2) # Third stride
shapes_2 = scale_shape_group(shapes_2, 1.0, 1.0, stride_len , 0.0)
walk_1stride(shapes_2) # Fourth stride

# Phase 3
# Shorten stride AGAIN length by x_amp = 0.7
stride_end = shapes_2[3][len(shapes_2[3])-2]
shapes_1 = copy.deepcopy(shapes) 
shapes_1 = scale_shape_group(shapes_1, 0.7*0.7*0.7, 0.3, 0.0, 0.0) #shapes_1 has now been reduced twice.
stride_len = shapes_1[3][len(shapes_1[3])-2]  - shapes_1[3][0] # new stride_len * 0.7 * 0.7
# Horizontal offset applied to accomodate next stride asd well as continue from last step.
shapes_2 = scale_shape_group(shapes_1, 1.0, 1.0, stride_end , 0.0)
walk_1stride(shapes_2) # Fifth stride
shapes_2 = scale_shape_group(shapes_2, 1.0, 1.0, stride_len , 0.0)
walk_1stride(shapes_2) # Sixth stride

# Phase 4
# Shorten stride AGAIN length by x_amp = 0.7
stride_end = shapes_2[3][len(shapes_2[3])-2]
shapes_1 = copy.deepcopy(shapes) 
shapes_1 = scale_shape_group(shapes_1, 0.7*0.7*0.7*0.7, 0.3, 0.0, 0.0) #shapes_1 has now been reduced twice.
stride_len = shapes_1[3][len(shapes_1[3])-2]  - shapes_1[3][0] # new stride_len * 0.7 * 0.7
# Horizontal offset applied to accomodate next stride asd well as continue from last step.
shapes_2 = scale_shape_group(shapes_1, 1.0, 1.0, stride_end , 0.0)
walk_1stride(shapes_2) # Seventh stride
shapes_2 = scale_shape_group(shapes_2, 1.0, 1.0, stride_len , 0.0)
walk_1stride(shapes_2) # Eighth stride

# Phase 5
# Shorten stride AGAIN length by x_amp = 0.7
stride_end = shapes_2[3][len(shapes_2[3])-2]
shapes_1 = copy.deepcopy(shapes) 
shapes_1 = scale_shape_group(shapes_1, 0.7*0.7*0.7*0.7*0.7, 0.3, 0.0, 0.0) #shapes_1 has now been reduced twice.
stride_len = shapes_1[3][len(shapes_1[3])-2]  - shapes_1[3][0] # new stride_len * 0.7 * 0.7
# Horizontal offset applied to accomodate next stride asd well as continue from last step.
shapes_2 = scale_shape_group(shapes_1, 1.0, 1.0, stride_end , 0.0)
walk_1stride(shapes_2) # Ninth stride
shapes_2 = scale_shape_group(shapes_2, 1.0, 1.0, stride_len , 0.0)
walk_1stride(shapes_2) # Tenth stride

root.mainloop()
