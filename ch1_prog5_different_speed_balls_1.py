""" 
Program name: different_rate_animation_balls_1.py
Objective: Make different balls travel at different speeds.

Keywords: canvas, ball, time, erase, movement, speed
============================================================================79
Comments: The speed of each ball is determined by the increment in position
on each loop execution cycle..

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine.
"""
from Tkinter import *
#from tkinter import *
import time
root = Tk()

cw = 800                                      # canvas width
ch = 80                                      # canvas height
                               
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

# Time Control variable
cycle_period1 = 10 # time between new positions of the ball (milliseconds).

# The parameters determining the dimensions of the ball and it's position.
posn_x1  =     1    # x position of box containing the ball (bottom). 
posn_y1  =     30   # x position of box containing the ball (left edge). 
shift_x1  =    1    # amount of x-movement each cycle of the 'for' loop.
shift_y1  =    1    # amount of y-movement each cycle of the 'for' loop.
ball_width1 =  15   # size of ball - width (x-dimension).
ball_height1 = 15   # size of ball - height (y-dimension).
color1 = "violet"   # color of the ball

# The parameters determining the dimensions of the ball and it's position.
posn_x2  =     1    # x position of box containing the ball (bottom). 
posn_y2  =     50   # x position of box containing the ball (left edge). 
shift_x2  =    1    # amount of x-movement each cycle of the 'for' loop.
shift_y2  =    1    # amount of y-movement each cycle of the 'for' loop.
ball_width2 =  15   # size of ball - width (x-dimension).
ball_height2 = 15   # size of ball - height (y-dimension).
color2 = "green"    # color of the ball

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# DRAWING AND ANIMATION
for i in range(1,500):       # end the program after 50 position shifts. 
    posn_x1 +=  shift_x1
    chart_1.create_oval(posn_x1, posn_y1, posn_x1 + ball_width1, posn_y1 + ball_height1, fill=color1)

    posn_x2 +=  shift_x2 + 0.5
    chart_1.create_oval(posn_x2, posn_y2, posn_x2 + ball_width2, posn_y2 + ball_height2, fill=color2)

    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period1)  # This makes execution pause for 200 milliseconds.
    chart_1.delete(ALL)           # This erases everything on the canvas 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

root.mainloop()
