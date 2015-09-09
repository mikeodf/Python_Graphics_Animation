""" 
Program name: two_gravityballs_tracer.py 
Objective: Two balls moving under the influence of gravity and leaving a trail 
showing the trajectory and history of each ball. 

Keywords: ball, bounce, gravity, time trace, movement, selective deletion 
============================================================================79 
Comments: To make the animation depiction work you need to erase the balls 
in their old position immediately before re-creating them in their new 
positions. The "canvas_1.delete("ball_x")" method achieves by deleting each 
ball in turn. The value in referring the each ball by its tag name to delete 
it is that you can selectively delete the balls but leave the trajectory 
lines untouched. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2   
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
root = Tk() 
root.title('Two balls Bouncing with Tracers') 
cw = 400                                     # canvas width 
ch = 400                                      # canvas height                         
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

GRAVITY = 1.5               # The 'strength' of gravity 
cycle_period = 80 
time_scaling = 0.2  # This governs the size of the differential steps 
                                # when calculating changes in position. 

# The parameters determining the dimensions of the ball and it's position. 
ball_1 = {'posn_x':25.0,              # x position of box containing the ball (bottom). 
           'posn_y':180.0,                 # x position of box containing the ball (left edge). 
           'velocity_x':30.0,              # amount of x-movement each cycle of the 'for' loop. 
           'velocity_y':100.0,            # amount of y-movement each cycle of the 'for' loop. 
           'ball_width':20.0,              # size of ball - width (x-dimension). 
           'ball_height':20.0,             # size of ball - height (y-dimension). 
           'color':"blue",                    # color of the ball 
           'coef_restitution':0.90}     # proportion of elastic enrgy recovered each bounce .

ball_2 = {'posn_x':cw - 25.0,        
           'posn_y':300.0,           
           'velocity_x':-50.0,       
           'velocity_y':150.0,        
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
    if ball_x['posn_x'] <  1:                             # Collision with left-hand  wall. 
       ball_x['velocity_x'] = -ball_x['velocity_x'] *  ball_x['coef_restitution'] 
       ball_x['posn_x'] = 2                              # anti-stick-to-the-wall 
    if ball_x['posn_y'] <   ball_x['ball_height'] :       # Collision with ceiling. 
       ball_x['velocity_y'] = -ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ball_x['ball_height'] * 1.1    # ceiling collision anti-stick 
    if ball_x['posn_y'] > ch - ball_x['ball_height'] * 1.1 :            # Floor collision.  
       ball_x['velocity_y'] = - ball_x['velocity_y'] *  ball_x['coef_restitution'] 
       ball_x['posn_y'] = ch -  ball_x['ball_height'] * 1.1   # anti-stick. Prevents out-of-bounds ball loss (stickiness) 
    
def diffEquation(ball_x): 
     """ 
     An approximate set of relationships representing the behavior of balls in gravity. 
     """ 
     x_old =  ball_x['posn_x'] 
     y_old =  ball_x['posn_y'] 
     ball_x['posn_x'] +=   ball_x['velocity_x'] * time_scaling 
     ball_x['velocity_y'] =  ball_x['velocity_y'] + GRAVITY        # A crude equation incorporating gravity. 
     ball_x['posn_y'] +=  ball_x['velocity_y'] * time_scaling 
     canvas_1.create_oval( ball_x['posn_x'],  ball_x['posn_y'],  ball_x['posn_x'] +  ball_x['ball_width'] 
     ,ball_x ['posn_y'] +  ball_x['ball_height'], fill= ball_x['color'], tags="ball_x") 
     canvas_1.create_line( x_old,  y_old,  ball_x['posn_x'], ball_x ['posn_y'], fill= ball_x['color']) 
     detectWallCollision(ball_x)                                  # Has the ball collided with any container wall? 


for i in range(1,5000):       # End the program after 500 position shifts.     
    diffEquation(ball_1) 
    diffEquation(ball_2) 

    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.         
    canvas_1.delete("ball_x")        # This erases everything on the canvas between 'movie frames' 

root.mainloop() 
