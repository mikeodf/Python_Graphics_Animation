"""
Program name: rotate_8link_line_1.py
Objective: Rotate eight lines, each at the tip of the next.

Keywords: canvas, line, rotation, time, movement, tip locus
============================================================================79
 Comments: For each line we need to specify its length and speed of rotation
as they are the main determinants of the patterns that emerge. Starting also
influences the pattern but to a lesser extent.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
import time
root = Tk()
root.title("Indego Song 1.")
import math

cw = 1000                                      # canvas width
ch = 1000                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 30 # time between new positions (milliseconds).

p0_x = 500.0
p0_y = 500.0

len1, len2, len3, len4, len5, len6, len7, len8 = 300.0, 80.0, 50.0, 20.0, 40.0, 100.0, 40.0, 60.0
alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

def tip_rotate(x_start, y_start, Length, alpha):
    """ give the tip position of a line with one end at x_start, y_start
        of length = Length and angular position alpha.
    """
    x_position = x_start + Length * math.cos(alpha)
    y_position = y_start + Length * math.sin(alpha)
    return x_position, y_position

for i in range(1,10000):       # end the program after 10000 position shifts.

    alpha1 += 0.006
    x1, y1 = tip_rotate(p0_x, p0_y, len1, alpha1) 

    alpha2 -= 0.01
    x2, y2 = tip_rotate(x1, y1, len2, alpha2)
    chart_1.create_line(x1, y1, x2, y2, tag='line_2', fill='#110033')

    alpha3 -= 0.01
    x3, y3 = tip_rotate(x2, y2, len3, alpha3)

    alpha4 += 0.02
    x4, y4 = tip_rotate(x3, y3, len4, alpha4)
    chart_1.create_line(x3, y3, x4, y4, tag='line_4', fill='#3914af')
    
    alpha5 += 0.05
    x5, y5 = tip_rotate(x4, y4, len5, alpha5)
    chart_1.create_line(x4, y4, x5, y5, tag='line_5', fill='#200772')

    #  The separate group of 3 line attached to line2 (x2, y2) 
    alpha6 += 0.015
    x6, y6 = tip_rotate(x2, y2, len6, alpha6)

    alpha7 -= 0.005
    x7, y7 = tip_rotate(x6, y6, len7, alpha7)
    chart_1.create_line(x6, y6, x7, y7, tag='line_7', fill='#071a71')
    
    alpha8 -= 0.05
    x8, y8 = tip_rotate(x7, y7, len8, alpha8)
    chart_1.create_line(x7, y7, x8, y8, tag='line_8', fill='#3e0470')  

    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 30 milliseconds.         

root.mainloop()
