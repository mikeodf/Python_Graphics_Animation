""" 
Program name: draw_pause_erase_shift_ball_1.py
Objective: Draw a ball in  a series of positions with pauses and deletions to achieve animation.

Keywords: canvas, ball, time, erase, movement
============================================================================79
Comments: Time control is introduced to produce crude animated movement.
The ball is drawn into a fresh position every 500 milliseconds.
A sense of movement results form the erasure through the ".delete(ALL)"
function provided in the "time" module.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine.
"""
from Tkinter import *
#from tkinter import *
import time
root = Tk()

cw = 200                                      # canvas width
ch = 200                                      # canvas height
                               
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

# Time Control variable
cycle_period = 50 # time between new positions of the ball (milliseconds).
 
# The parameters determining the dimensions of the ball and it's position.
posn_x  =     1    # x position of box containing the ball (bottom). 
posn_y  =     1    # x position of box containing the ball (left edge). 
shift_x  =    1    # amount of x-movement each cycle of the 'for' loop.
shift_y  =    1    # amount of y-movement each cycle of the 'for' loop.
ball_width =  15   # size of ball - width (x-dimension).
ball_height = 15   # size of ball - height (y-dimension).
color = "violet"   # color of the ball

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# DRAWING AND ANIMATION
for i in range(1,500):       # end the program after 50 position shifts. 
    posn_x +=  shift_x
    posn_y +=  shift_y

    chart_1.create_oval(posn_x, posn_y, posn_x + ball_width, posn_y + ball_height, fill=color)
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    chart_1.delete(ALL)           # This erases everything on the canvas 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

root.mainloop()
