""" 
Program name: drawball_1.py
Objective: Draw a ball.

Keywords: canvas, ball
============================================================================79
Comments: The object to be animated will be green ball 15 pixels in diameter. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine.
"""
from Tkinter import *
#from tkinter import *
root = Tk()

cw = 150                                      # canvas width
ch = 150                                      # canvas height                               
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)
 
# The parameters determining the dimensions of the ball and it's position.
posn_x  =     1     # x position of box containing the ball (bottom) 
posn_y  =     1     # x position of box containing the ball (left edge) 
shift_x  =    10    # amount of x-movement each cycle of the 'for' loop
shift_y  =    10    # amount of y-movement each cycle of the 'for' loop
ball_width =  15    # size of ball - width (x-dimension)
ball_height = 15    # size of ball - height (y-dimension)
color = "green"    # color of the ball

chart_1.create_oval(posn_x, posn_y, posn_x + ball_width, posn_y + ball_height, fill=color)

root.mainloop()
