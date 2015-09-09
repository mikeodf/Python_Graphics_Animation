""" 
Program name: collision_loss_gravityball_1.py 
Objective: Draw a ball under the influence of gravity and energy loss 
with every bounce. 

Keywords: canvas, ball, bounce, gravity, energy loss, restitution, time, movement 
============================================================================79 
Explanation: The equation of motion that includes the influence of gravity as 
well as a proportion of elastic energy loss with each collision. 
Note: When the ball has stopped bouncing it gradually slides below floor level.
This is because we have not included a statement to prevent this - it is good
to be aware of this problem in well designed simulations.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2   
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
import time 
root = Tk() 
root.title('Ball bouncing with energy loss on collision.') 
cw = 800                                      # canvas width 
ch = 500                                      # canvas height 
                          
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period   = 30 # Time between new positions of the ball (milliseconds). 
time_increment = 0.2 
GRAVITY = 10     
# The parameters determining the dimensions of the ball and it's position. 
posn_x      =     15     # x position of box containing the ball (bottom). 
posn_y      =     180    # x position of box containing the ball (left edge). 
velocity_x  =     20 
velocity_y  =     50        
ball_diameter =   30     # Size of ball - width (x-dimension). 
coef_restitution = 0.8   # Proportion of elastic energy recovered each bounce 
color = "blue"           # Color of the ball 

# Here is a function that detects collisions with the walls of the container 
# and then reverses the direction of movement if a collision is detected. 
def detectWallCollision(ball_diameter, coef_restitution, posn_x, posn_y, velocity_x, velocity_y, cw, ch): 
    """ Detects collisions with the walls of the container, reverse the direction
        of velocity if a collision is detected and subtract a proportion of energy
        with every collision.. 
    """ 
    if posn_x > cw - ball_diameter:                 # Collision with right-hand container wall. 
	velocity_x = -velocity_x * coef_restitution # Reverse direction and lose energy. 
    if posn_x <  0:                     # Collision with left-hand  wall. 
	velocity_x = -velocity_x * coef_restitution  
    if posn_y <  ball_diameter :                   # Collision with ceiling. 
	velocity_y = -velocity_y * coef_restitution 
    if posn_y > ch - ball_diameter :               # Floor collision. 
	velocity_y = -velocity_y * coef_restitution 
        posn_y = ch - ball_diameter 
    return velocity_x, velocity_y


for i in range(1, 5000):       # End the program after 5000 position shifts. 
    posn_x     += velocity_x * time_increment 
    velocity_y += GRAVITY * time_increment          # Gravity changes velocity. 
    posn_y     += velocity_y * time_increment       # Velocity changes position. 
    print velocity_y 
    canvas_1.create_oval(posn_x, posn_y, posn_x + ball_diameter, posn_y + ball_diameter, fill=color) 
    velocity_x, velocity_y = detectWallCollision(ball_diameter, coef_restitution, posn_x, posn_y, velocity_x, velocity_y, cw, ch)                # Has the ball collided with any container wall? 
    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)         # This makes execution pause for 200 milliseconds. 
    canvas_1.delete(ALL)                 # This erases everything on the canvas. 
root.mainloop() 
