""" 
Program name: rotate_line_3D_1 .py 
Objective: Rotate a single line in 3 dimensions. 

Keywords: canvas, line, time, movement, rotation, 3D 
=====================================================================79 
Comments: Animate the rotation of a line in 3 Dimensions.. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine 

""" 
from Tkinter import * 
#from tkinter import *  # For Python version 3..2 or higher.

import time 
import math 
root = Tk() 
root.title("Rotating 3D line: a=0360, b=0005") 

cw = 360                                      # canvas width 
ch = 330                                      # canvas height 
chart_1 = Canvas(root, width=cw, height=ch, background="white") 
chart_1.grid(row=0, column=0) 

cycle_period = 20       # pause duration (milliseconds). 

p1_x = 90.0 
p1_y = 90.0 
p1_z = 0

p2_x = 180.0 
p2_y = 160.0 

trail_x = 180.0 
trail_y = 160.0 

a_radian = math.atan((p2_y - p1_y)/(p2_x - p1_x)) 
a_length = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +  (p2_x - p1_x)*(p2_x - p1_x)) 
b_radian  = 0.0

for i in range(1,500):       # end the program after 500 position shifts. 
    
    a_radian +=0.0360 
    b_radian +=0.0005
    trail_x = p1_x 
    trail_y = p1_y 

    p1_x = p2_x - a_length * math.cos(a_radian) * math.cos(b_radian)
    p1_y = p2_y - a_length * math.sin(a_radian) 
    p1_z = p2_y - a_length * math.cos(a_radian) * math.sin(b_radian) 

    chart_1.create_line(trail_x, trail_y, p1_x, p1_y, width=1, fill='green') 
    chart_1.create_line(p1_x, p1_y, p2_x, p2_y,tag='line_1',) 
    chart_1.update()              
    chart_1.after(cycle_period)  
    chart_1.delete('line_1')          
root.mainloop() 
