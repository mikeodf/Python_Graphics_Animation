"""
Program name: legs_walking_repeated stride_1.py
Objective: Animate a rudimentary walking stride with repeated steps.

Keywords: canvas, legs, walking, repeated stride stride
============================================================================79 
Comments: The hip, knee,and foot positions are were derived from Inkscape sketches.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import math
import time
#import copy
root = Tk()
root.title("Designer Walks: walks with limp.") 

cw = 1000                                   # canvas width
ch = 500                                   # canvas height
                             
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
  
def draw_walker(indx):
    """ Draw entire body as a stick man.
    """
    chart_1.create_oval(hips[indx]-6, hips[indx+1]-6,hips[indx]+6, hips[indx+1]+6, fill= "magenta", width = 1, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], knee_a[indx], knee_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], knee_b[indx], knee_b[indx+1], fill= "green", width = 2, tag = 'line_1') 
    chart_1.create_line(knee_a[indx], knee_a[indx+1], heel_a[indx], heel_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(knee_b[indx], knee_b[indx+1], heel_b[indx], heel_b[indx+1], fill= "green", width = 2, tag = 'line_1') 

def walk_1stride():
    """  Walk one stride.
    """
    for i in range(len(hips)/2):
        draw_walker(2*i)
        animdelay()
#======================================================================
# Test and Demonstrate
stride_len = heel_a[len(heel_a)-2]  - heel_a[0]

walk_1stride() # First stride

# Advance every joint by one stride length. 
hips = scale_shape(hips, 1.0, 1.0, stride_len, 0.0)
heel_a = scale_shape(heel_a, 1.0, 1.0, stride_len, 0.0)
knee_a = scale_shape(knee_a, 1.0, 1.0, stride_len, 0.0)
heel_b = scale_shape(heel_b, 1.0, 1.0, stride_len, 0.0)
knee_b = scale_shape(knee_b, 1.0, 1.0, stride_len, 0.0)

walk_1stride() #Second stride

root.mainloop()
