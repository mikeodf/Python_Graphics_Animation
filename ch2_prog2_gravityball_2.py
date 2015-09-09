""" 
Program name: gravityball_2.py 
Objective: Draw a ball under the influence of gravity. 

Keywords: canvas, ball, bounce, gravity, time, movement 
============================================================================79 
Explanation: The equation of motion that includes the influence 
of gravity. Note that because of the conventions used for screen(canvas) 
reference positions the acceleration due to gravity has a plus sign. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2   
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
import time 
root = Tk() 
root.title('Integer position for balls') 
cw = 800                                      # canvas width 
ch = 500                                      # canvas height 
                          
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period   = 30 # Time between new positions of the ball (milliseconds). 
time_increment = 0.2 
GRAVITY = 10     
# The parameters determining the dimensions of the ball and it's position. 
posn_x      =     50     # x position of box containing the ball (bottom). 
posn_y      =     180    # y position of box containing the ball (left edge). 
velocity_x  =     20 
velocity_y  =     50        
ball_diameter =   50      # Size of ball - width (x-dimension). 
color = "blue"            # Color of the ball 


def detectWallCollision(ball_diameter, posn_x, posn_y, velocity_x, velocity_y, cw, ch ):
    """ Detect collisions with the walls of the container
       and then reverses the direction of movement if a collision is detected. 
    """
    if posn_x > cw - ball_diameter:         # Collision with right-hand container wall. 
	velocity_x = -velocity_x            
    if posn_x <=  0:                        # Collision with left-hand  wall. 
	velocity_x = -velocity_x 
    if posn_y <  ball_diameter :            # Collision with ceiling. 
	velocity_y = -velocity_y 
    if posn_y > ch - ball_diameter :        # Floor collision. 
	velocity_y = -velocity_y 
    return velocity_x, velocity_y
#=========================================================
# Execution and Test
for i in range(1, 15000):                        # End the program after 1500 position shifts. 
    posn_x     += velocity_x * time_increment 
    velocity_y += GRAVITY * time_increment       # Gravity changes velocity. 

    posn_y     += velocity_y * time_increment       # Velocity changes position. 
    canvas_1.create_oval(posn_x, posn_y, posn_x + ball_diameter, posn_y + ball_diameter, fill=color) 
    velocity_x, velocity_y = detectWallCollision(ball_diameter, posn_x, posn_y, velocity_x, velocity_y, cw, ch ) # Has the ball collided with any container wall? 
    print velocity_y    
    canvas_1.update()                     # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)          # This makes execution pause for 200 milliseconds. 
    canvas_1.delete(ALL)                  # This erases everything on the canvas. 
root.mainloop()   
