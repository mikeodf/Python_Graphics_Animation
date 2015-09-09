""" 
Program name: ball_with_air_resistance_1.py 
Objective: Compare trajectories with and without air resistance. 

Keywords: canvas, cannon, gravity, air resistance, time, movement, animation 
============================================================================79 
Explanation: The grey ball experiences no airresistance while the blue ball 
experiences a Stokes law type of resistance where the drag force is 
proportional to the square of the velocity. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
import math 
root = Tk() 
root.title("Ball Trajectories With Air Resistance") 
cw = 800                                     # canvas width 
ch = 550                                     # canvas height                         
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 
 
GRAVITY = 1.8               # The strength of gravity 
cycle_period = 20 
time_scaling = 0.1  # This governs the size of the differential steps 
                                # when calculating changes in position. 

# The parameters determining the dimensions of the ball and it's position. 
# This ball experiences air resistance. 
ball_1 = {'posn_x':25.0,              # x position of box containing the ball (bottom). 
           'posn_y':780.0,                 # x position of box containing the ball (left edge). 
           'velocity_x':40.0,              # amount of x-movement each cycle of the 'for' loop. 
           'velocity_y':-160.0,          # amount of y-movement each cycle of the 'for' loop. 
           'ball_width':20.0,             # size of ball - width (x-dimension). 
           'ball_height':20.0,            # size of ball - height (y-dimension). 
           'color':"blue",                   # color of the ball 
           'air_resistance':0.000015, 
           'coef_restitution':0.90}    # proportion of elastic energy recovered each bounce 

# This ball experiences no air resistance. 
ball_2 = {'posn_x':25.0,    
           'posn_y':780.0,    
           'velocity_x':40.0, 
           'velocity_y':-160.0,    
           'ball_width':20.0,  
           'ball_height':20.0,  
           'color':"grey",  
           'air_resistance':0.0, 
           'coef_restitution':0.90} 

def detectWallCollision(ball_x): 
    """ Detects collisions with the walls of the container 
        and then reverses the direction of movement is a collision is detected. 
    """  
    if ball_x['posn_x'] > cw -  ball_x['ball_width']:       # Collision with right-hand container wall. 
        ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution']      # reverse direction. 
        ball_x['posn_x'] = cw -  ball_x['ball_width'] * 1.1      # anti-stick to the wall 
    if  ball_x['posn_x'] <  1:                             # Collision with left-hand  wall. 
        ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution'] 
        ball_x['posn_x'] = 2                              # anti-stick-to-the-wall 
    if  ball_x['posn_y'] <   ball_x['ball_height'] :       # Collision with ceiling. 
        ball_x['velocity_y'] = -ball_x['velocity_y'] *  ball_x['coef_restitution'] 
        ball_x['posn_y'] = ball_x['ball_height'] * 1.1    # ceiling collision anti-stick 
    if  ball_x['posn_y'] > ch - ball_x['ball_height'] * 1.1 :            # Floor collision.  
        ball_x['velocity_y'] = - ball_x['velocity_y'] *  ball_x['coef_restitution'] 
        ball_x['posn_y'] = ch -  ball_x['ball_height'] * 1.1   # anti-stick. Prevents out-of-bounds ball loss (stickiness) 
    
def diffEquation(ball_x): 
     """  Relationships governing the behavior of the balls. 
     """ 
     x_old =  ball_x['posn_x'] 
     y_old =  ball_x['posn_y'] 
     ball_x['posn_x'] +=   ball_x['velocity_x'] * time_scaling 
     ball_x['velocity_y'] =  ball_x['velocity_y'] + GRAVITY # a crude equation incorporating gravity. 
     # loss of speed due to air resistance. 
     speed_squared = ball_x['velocity_y']*ball_x['velocity_y']+ ball_x['velocity_x']*ball_x['velocity_x'] 
     speed = math.sqrt(speed_squared) 
     air_drag = ball_x['air_resistance'] * speed_squared 
     speed = speed - air_drag 
     traj_angle = math.atan2(ball_x['velocity_y'],ball_x['velocity_x']) 
     angle_deg = traj_angle * 180/math.pi 
     # Resulting velocities after accounting for air resistance 
     ball_x['velocity_y'] = speed * math.sin(traj_angle) 
     ball_x['velocity_x'] = speed * math.cos(traj_angle) 
     # Resulting positionss after accounting for air resistance 
     ball_x['posn_y'] +=  ball_x['velocity_y'] * time_scaling 
     canvas_1.create_oval( ball_x['posn_x'],  ball_x['posn_y'],  ball_x['posn_x'] +  ball_x['ball_width'] 
     ,ball_x ['posn_y'] +  ball_x['ball_height'], fill= ball_x['color'], tags="ball_x") 
     canvas_1.create_line( x_old,  y_old,  ball_x['posn_x'], ball_x ['posn_y'], fill= ball_x['color'], width=2) 
     detectWallCollision(ball_x)                          # Has the ball collided with any container wall? 

for i in range(1,5000):       # End the program after 5000 position shifts.     
    diffEquation(ball_1) 
    diffEquation(ball_2) 

    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)   # This makes execution pause for 20 milliseconds.         
    canvas_1.delete('ball_x')           # This erases everything on the canvas between 'movie frames' 

root.mainloop() 
