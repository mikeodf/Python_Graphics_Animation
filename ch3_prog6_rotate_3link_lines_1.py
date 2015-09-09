"""
Program name: rotate_3link_lines_1.py
Objective: Rotate three lines, each at the tip of the next.

Keywords: canvas, line, rotation, time, movement, tip locus
============================================================================79
Comment: This code introduces the concept, in an abstract way, of relative
coordinate reference system. the center of rotation of each line segment
is at the tip of the previous line.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine

"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
import time
root = Tk()
root.title("Rotary rose.")
import math

cw = 1000                                      # canvas width
ch = 1000                                      # canvas height

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 50 # time between new positions of the ball (milliseconds).

def tip_rotate(x_start, y_start, Length, alpha):
    """ give the tip position of a line with one end at x_start, y_start
        of length = Length and angular position alpha.
    """
    x_position = x_start + Length * math.cos(alpha)
    y_position = y_start + Length * math.sin(alpha)
    return x_position, y_position

start_x = 500.0
start_y = 500.0

len1, len2, len3 = 300.0, 80.0, 50.0

alpha1, alpha2, alpha3 = 0.0, 0.0, 0.0

x2_old, y2_old, x3_old, y3_old =  0,0, 0,0

for i in range(1,4000):       # end the program after 500 position shifts.

    alpha1 += 0.01
    x1, y1 = tip_rotate(start_x, start_y, len1, alpha1) 

    alpha2 -= 0.007
    x2, y2 = tip_rotate(x1, y1, len2, alpha2)
    chart_1.create_line(x1, y1, x2, y2, tag='line_2', fill='#920031')
    x2_old, y2_old = x2, y2

    alpha3 -= 0.03
    x3, y3 = tip_rotate(x2, y2, len3, alpha3)
    chart_1.create_line(x2, y2, x3, y3, tag='line_3', fill='#a40004')
    x3_old, y3_old = x3, y3

   
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 50 milliseconds.        

root.mainloop()
