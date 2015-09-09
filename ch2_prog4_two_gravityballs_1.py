""" 
Program name: two_gravityballs_1 .py 
Objective: Two balls moving under the influence of gravity. 
Dictionaries have been used to handle ball object variables. 

Keywords: canvas, ball, bounce, gravity, time, movement 
============================================================================79 
Comments: A dictionary assigned to each ball provides a data structure that
is identical for any number of balls but maintains the unique property 
values for each separate ball. A generalized but approximate "differential equation"
function ( diffEquation(ball_x) ), maintains the dynamic (physics) relationships
that govern each ball's motion.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2   
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
root = Tk() 
root.title('Two balls Bouncing in Gravity') 
cw = 400                                     # canvas width 
ch = 400                                      # canvas height 

GRAVITY = 1.5                             
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period = 80 # Time between new positions of the ball (milliseconds). 
time_scaling = 0.2  # This governs the size of the differential steps 
                                # when calculating changes in position. 

# The parameters determining the dimensions of the ball and it's position and
# all other unique properties. 
ball_1 = {'posn_x':25.0,          # x position of box containing the ball (bottom). 
           'posn_y':180.0,        # x position of box containing the ball (left edge). 
           'velocity_x':30.0,     # amount of x-movement each cycle of the 'for' loop. 
           'velocity_y':100.0,    # amount of y-movement each cycle of the 'for' loop. 
           'ball_width':20.0,     # size of ball - width (x-dimension). 
           'ball_height':20.0,    # size of ball - height (y-dimension). 
           'color':"blue",            # color of the ball 
           'coef_restitution':0.90}   # proportion of elastic enrgy recovered each bounce . 

ball_2 = {'posn_x':cw - 25.0,     
           'posn_y':300.0,    
           'velocity_x':-50.0,  
           'velocity_y':150.0,   
           'ball_width':30.0,  
           'ball_height':30.0,  
           'color':"green",  
           'coef_restitution':0.90} 

# The argument 'ball_x' below is something of a dummy (placeholder). 
def detectWallCollision(ball_x): 
    """ 
    Detect collisions with the walls of the container 
    and then reverses the direction of movement is a collision is detected. 
    """ 
    if ball_x['posn_x'] > cw -  ball_x['ball_width']:       # Collision with right-hand container wall. 
       ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution']      # reverse direction. 
       ball_x['posn_x'] = cw -  ball_x['ball_width'] * 1.1      # anti-stick to the wall 
    if ball_x['posn_x'] <  1:                              # Collision with left-hand  wall. 
       ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution'] 
       ball_x['posn_x'] = 2                               # anti-stick to the wall 
    if ball_x['posn_y'] <   ball_x['ball_height'] :            # Collision with ceiling. 
       ball_x['velocity_y'] = -ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ball_x['ball_height'] * 1.1     # ceiling collision anti-stick 
    if ball_x['posn_y'] > ch - ball_x['ball_height'] * 1.1 :            # Floor collision.  
       ball_x['velocity_y'] = - ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ch -  ball_x['ball_height'] * 1.1   # anti-stick. Prevents out-of-bounds ball loss (stickiness) 
    
def diffEquation(ball_x): 
     """ The approximate physical relationships governing free motion of inelastic
         bouncing balls. The balls do not interact with each other.
     """
     ball_x['posn_x'] +=   ball_x['velocity_x'] * time_scaling 
     ball_x['velocity_y'] =  ball_x['velocity_y'] + GRAVITY  # a crude equation incorporating gravity. 
     ball_x['posn_y'] +=  ball_x['velocity_y'] * time_scaling 
     canvas_1.create_oval( ball_x['posn_x'],  ball_x['posn_y'],  ball_x['posn_x'] +  ball_x['ball_width'] 
     ,ball_x ['posn_y'] +  ball_x['ball_height'], fill= ball_x['color']) 
     detectWallCollision(ball_x)         # Has the ball collided with any container wall? 

for i in range(1,5000):                   # end the program after 5000 position shifts.   
    diffEquation(ball_1) 
    diffEquation(ball_2) 
    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)         # This makes execution pause for 200 milliseconds. 
    canvas_1.delete(ALL)                 # This erases everything on the canvas. 

root.mainloop() 
