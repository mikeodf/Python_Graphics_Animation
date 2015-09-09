""" 
Program name: gravityball_1.py 
Objective: Draw a ball under the influence of gravity and demonstrate the problem of integers. 

Keywords: canvas, ball, bounce, gravity, time, movement 
============================================================================79 
comments: A simplified equation of motion that includesed the influence 
of gravity is incorporated. Note that because of the conventions used 
for screen(canvas) reference positions, the acceleration due to gravity 
has a plus sign. 
The declaration of global variables inside a function definition is not
good programming practice. It is nevethe less good to know about.
The fact that we are using integer arithmetic only, causes the ball to dissappear 
off the bottom of the screen when the bounces become small. The collision 
detection criteria is too coarse when integers are used. We should use floating 
point. However screen position coordinates are integer so care must be exercised. 
"gravityball_2.py" tackles this issue. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2   
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
root = Tk() 
root.title('Integer position for balls') 
cw = 400                                      # canvas width 
ch = 400                                      # canvas height 
GRAVITY = 4                               
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period = 30 # Time between new positions of the ball (milliseconds). 

# The parameters determining the dimensions of the ball and it's position. 
posn_x  =     15.0     # x position of box containing the ball (bottom). 
posn_y  =     180.0    # y  position of box containing the ball (left edge). 
shift_x  =    1.0      # amount of x-movement each cycle of the 'for' loop. 
velocity_y  =  50.0    # amount of y-movement each cycle of the 'for' loop. 
ball_width =  12.0     # size of ball - width (x-dimension). 
ball_height = 12.0     # size of ball - height (y-dimension). 
color = "blue"         # color of the ball 

# Here is a function that detects collisions with the walls of the container 
# and then reverses the direction of movement is a collision is detected. 
def detectWallCollision(): 
    global posn_x, posn_y, shift_x, velocity_y, cw, cy    
    if posn_x > cw -ball_width:         # Collision with right-hand container wall. 
        shift_x = -shift_x              # Reverse direction. 
    if posn_x <  ball_width:            # Collision with left-hand  wall. 
        shift_x = -shift_x 
    if posn_y <  ball_height :          # Collision with ceiling. 
        velocity_y = -velocity_y 
    if posn_y > ch - ball_height :      # Floor collision. 
        velocity_y = -velocity_y 

for i in range(1,500):       # End the program after 500 position shifts. 
    posn_x +=  shift_x 
    velocity_y = velocity_y + GRAVITY  # a crude equation incorporating gravity. 
    posn_y +=  velocity_y 
    canvas_1.create_oval(posn_x, posn_y, posn_x + ball_width, posn_y + ball_height, fill=color) 
    detectWallCollision()              # Has the ball collided with any container wall? 
    canvas_1.update()                  # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)       # This makes execution pause for 30 milliseconds. 
    canvas_1.delete(ALL)               # This erases everything on the canvas.
root.mainloop() 
