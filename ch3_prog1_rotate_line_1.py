""" 
Program name: rotate_line_1 .py 
Objective: Rotate a single line. 

Keywords: canvas, line, time, movement 
=====================================================================79 
Motivation: Establish facility with the trigonometry of the requirements. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine 

""" 
from Tkinter import * 
#from tkinter import *  # For Python version 3.2 and higher.
import math 
root = Tk() 
root.title("Rotating line") 

cw = 220                                      # canvas width 
ch = 180                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period = 50       # pause duration (milliseconds). 

p1_x = 90.0 
p1_y = 90.0 

p2_x = 180.0 
p2_y = 160.0 

a_radian = math.atan((p2_y - p1_y)/(p2_x - p1_x)) 
a_length = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +  (p2_x - p1_x)*(p2_x - p1_x)) 

for i in range(1,300):       # end the program after 300 position shifts. 
    
    a_radian +=0.05 
    p1_x = p2_x - a_length * math.cos(a_radian) 
    p1_y = p2_y - a_length * math.sin(a_radian) 

    canvas_1.create_line(p1_x, p1_y, p2_x, p2_y) 
    canvas_1.update()              
    canvas_1.after(cycle_period)  
    canvas_1.delete(ALL)          
root.mainloop() 
