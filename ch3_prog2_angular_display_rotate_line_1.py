"""
Program name: angular_display_rotate_line_1 .py
Objective: Rotate a single line.

Keywords: canvas, line, time, movement
============================================================================79
recipe # 9 
Explanation: Establish facility with the trigonometry of the requirements.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine

"""
# rotate_line_1.py
from Tkinter import *
import time
import math
root = Tk()
root.title("Rotating line with angle display")

cw = 420                                      # canvas width
ch = 320                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 500# pause duration (milliseconds).

tip_x = 106.07 + 150.0
tip_y = 150.0 -  106.07
pivot_x = 150.0
pivot_y = 150.0
a_radian = math.atan2((tip_y - pivot_y), (tip_x - pivot_y))
a_length = math.sqrt((tip_y - pivot_y)*(tip_y - pivot_y) +  (tip_x - pivot_x)*(tip_x - pivot_x))

for i in range(1,300):       # end the program after 300 position shifts.
    
    a_radian +=0.05
    tip_x = pivot_x + a_length * math.cos(a_radian)
    tip_y = pivot_y + a_length * math.sin(a_radian)
    a_length = math.sqrt((tip_y - pivot_y)*(tip_y - pivot_y) +  (tip_x - pivot_x)*(tip_x - pivot_x))
    a_radian = math.atan2((tip_y - pivot_y), (tip_x - pivot_y))
    a_degrees = str(math.degrees(a_radian)) 
    chart_1.create_text(100,20, text = a_degrees)

    chart_1.create_line(pivot_x, pivot_y, tip_x, tip_y)
    chart_1.update()              
    chart_1.after(cycle_period)  
    chart_1.delete(ALL)    
     
root.mainloop()

