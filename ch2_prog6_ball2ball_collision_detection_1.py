""" 
Program name: ball2ball_collision_detection_1 .py 
Objective: Detect and react to inter-ball collisions. 

Keywords: ball, bounce, gravity, time, movement, mutual impact, collision 
============================================================================79 
Comments: The idea behind ball-to-ball collision detection is to sweep 
the canvas with an imaginary vertical strip containing one ball and test 
if there is another ball inside this strip. If there is then sweep through 
that strip and test if there is a ball very close to the original one. 
If there is then a collision can be judged to have occured and the directions 
of velocity of the colliding balls should bereversed. 
Note that this is a relatively crude approximation. For accurate impact 
rebound calculation, the direction of rebound should take into account 
exactly where the ball surfaces touch each other to generate a rebound impact 
force that is normal to the colliding surfaces. This is too complicated 
for these examples. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
import math 
root = Tk() 
root.title('Collision Detection Between Balls') 
cw = 400                                     # canvas width 
ch = 400                                      # canvas height 

GRAVITY = 1.5                             
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period = 80   # Time between new positions of the ball (milliseconds). 
time_scaling = 0.2  # This governs the size of the differential steps 
                                # when calculating changes in position. 

# The parameters determining the dimensions of the ball and it's position. 
ball_1 = {'posn_x':25.0,            # x position of box containing the ball (bottom). 
           'posn_y':25.0,                 # x position of box containing the ball (left edge). 
           'velocity_x':65.0,            # amount of x-movement each cycle of the 'for' loop. 
           'velocity_y':50.0,            # amount of y-movement each cycle of the 'for' loop. 
           'ball_width':20.0,            # size of ball - width (x-dimension). 
           'ball_height':20.0,           # size of ball - height (y-dimension). 
           'color':"blue",                  # color of the ball 
           'coef_restitution':0.90}   # proportion of elastic enrgy recovered each bounce 

ball_2 = {'posn_x':cw - 25.0,     
           'posn_y':380.0,    
           'velocity_x':-50.0, 
           'velocity_y':-70.0,  
           'ball_width':30.0,   
           'ball_height':30.0,  
           'color':"green",   
           'coef_restitution':0.90}  

def detectWallCollision(ball_x): 
    """ 
    Detect collisions with the walls of the container 
    and then reverses the direction of movement is a collision is detected. 
    """    
    if ball_x['posn_x'] > cw -  ball_x['ball_width']:       # Collision with right-hand container wall. 
       ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution']      # reverse direction. 
       ball_x['posn_x'] = cw -  ball_x['ball_width'] * 1.1      # anti-stick to the wall 
    if ball_x['posn_x'] <  1:             # Collision with left-hand  wall. 
       ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution'] 
       ball_x['posn_x'] = 2      # anti-stick to the wall 
    if ball_x['posn_y'] <   ball_x['ball_height'] :            # Collision with ceiling. 
       ball_x['velocity_y'] = -ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ball_x['ball_height'] * 1.1    # ceiling collision anti-stick 
    if ball_x['posn_y'] > ch - ball_x['ball_height'] * 1.1 :            # Floor collision.  
       ball_x['velocity_y'] = - ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ch -  ball_x['ball_height'] * 1.1    # anti-stick. Prevents out-of-bounds ball loss (stickiness) 


def detectBallCollision(ball_x, ball_2): 
    """ Detect ball-to-ball collision 
        firstly: is there a close approach in the horizontal direction. 
    """ 
    if math.fabs(ball_x['posn_x'] - ball_2['posn_x']) < 25: 
        # secondly: is there also a close approach in the horizontal direction 
        if math.fabs(ball_x['posn_y'] - ball_2['posn_y']) < 25: 
            ball_x['velocity_x'] = -ball_x['velocity_x'] # reverse direction. 
            ball_x['velocity_y'] = -ball_x['velocity_y'] # reverse direction. 
            ball_2['velocity_x'] = -ball_2['velocity_x'] # reverse direction. 
            ball_2['velocity_y'] = -ball_2['velocity_y'] # reverse direction. 
            # to avoid internal rebounding inside balls 
            ball_x['posn_x'] +=   ball_x['velocity_x'] * time_scaling 
            ball_x['posn_y'] +=   ball_x['velocity_y'] * time_scaling 
            ball_2['posn_x'] +=   ball_2['velocity_x'] * time_scaling 
            ball_2['posn_y'] +=   ball_2['velocity_y'] * time_scaling 

def diffEquation(ball_x): 
     """ 
     An approximate set of relationships representing the behavior of balls in gravity. 
     """ 
     x_old =  ball_x['posn_x'] 
     y_old =  ball_x['posn_y'] 
     ball_x['posn_x'] +=   ball_x['velocity_x'] * time_scaling 
     ball_x['velocity_y'] =  ball_x['velocity_y'] + GRAVITY  # a crude equation incorporating gravity. 
     ball_x['posn_y'] +=  ball_x['velocity_y'] * time_scaling 
     canvas_1.create_oval( ball_x['posn_x'],  ball_x['posn_y'],  ball_x['posn_x'] +  ball_x['ball_width'] 
     ,ball_x ['posn_y'] +  ball_x['ball_height'], fill= ball_x['color'], tags="ball_x") 
     canvas_1.create_line( x_old,  y_old,  ball_x['posn_x'], ball_x ['posn_y'], fill= ball_x['color']) 
     detectWallCollision(ball_x)         # Has the ball collided with any container wall? 

# Main simulation loop. 
for i in range(1,5000):       # End the program after 5000 position shifts. 
    diffEquation(ball_1) 
    diffEquation(ball_2) 
    detectBallCollision(ball_1, ball_2) 
    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)   # This makes execution pause for 80 milliseconds.         
    canvas_1.delete("ball_x")        # This erases everything on the canvas 

root.mainloop() 
