""" 
Program name: ball_collisions_class_1.py 
Objective: Two balls moving under the influence of gravity. 

Keywords: canvas, class, ball, bounce, gravity, time, movement 
============================================================================79 
Explanation: A simplified equation of motion that inclused the influence of gravity in incorporated. Note that because of the conventions used for screen(canvas) reference positions the acceleration due to gravity 
has a plus sign. 
There is a numerical loss of 'energy' each time the ball hits a barrier 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2  
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher.
root = Tk() 
root.title("Ball Collisions using Classes") 
cw = 350                                     # canvas width 
ch = 300                                      # canvas height 

GRAVITY = 1.5                             
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=0) 
 
cycle_period = 80   # Time between new positions of the ball (milliseconds). 
time_scaling = 0.2  # This governs the size of the differential steps 
                                # when calculating changes in position. 

class BallBounce: 
    """ The behaviors and properties of bouncing balls. 
    """ 
    def __init__(self, posn_x, posn_y, velocity_x, velocity_y, kula): 
        """ Initialize values at instantiation. 
        """ 
        self.posn_x = posn_x              # x position of box containing the ball (bottom). 
        self.posn_y = posn_y              # x position of box containing the ball (left edge). 
        self.velocity_x = velocity_x    # amount of x-movement each cycle of the 'for' loop. 
        self.velocity_y = 100.0            # amount of y-movement each cycle of the 'for' loop. 
        self.color = kula                       # color of the ball 

        self.ball_width  = 20.0         # size of ball - width (x-dimension). 
        self.ball_height = 20.0         # size of ball - height (y-dimension). 
        self.coef_restitution = 0.90 

    def detectWallCollision(self): 
        """  Collision detection with the walls of the container  
        """ 
        if self.posn_x > cw -  self.ball_width:                  # Collision with right-hand container wall. 
           self.velocity_x = -self.velocity_x * self.coef_restitution     # reverse direction. 
           self.posn_x = cw -  self.ball_width * 1.1                      # anti-stick to the wall 
        if self.posn_x <  1:                                               # Collision with left-hand  wall. 
           self.velocity_x = -self.velocity_x *  self.coef_restitution 
           self.posn_x = 2                                                # anti-stick to the wall 
        if self.posn_y <   self.ball_height:                               # Collision with ceiling. 
           self.velocity_y = -self.velocity_y *  self.coef_restitution 
           self.posn_y = self.ball_height * 1.1                           # ceiling collision anti-stick 
        if self.posn_y > ch - self.ball_height * 1.1 :                     # Floor collision.  
           self.velocity_y = - self.velocity_y *  self.coef_restitution 
           self.posn_y = ch -  self.ball_height * 1.1                 # anti-stick. Prevents out-of-bounds ball loss (stickiness) 
     
    def diffEquation(self): 
         """  An approximate set of differential equations of motion for the balls 
         """ 
         self.posn_x +=   self.velocity_x * time_scaling 
         self.velocity_y =  self.velocity_y + GRAVITY  # a crude equation incorporating gravity. 
         self.posn_y +=  self.velocity_y * time_scaling 
         canvas_1.create_oval( self.posn_x,  self.posn_y,  self.posn_x +  self.ball_width, 
                        self.posn_y +  self.ball_height, fill= self.color) 
         self.detectWallCollision()         # Has the ball collided with any container wall? 

# Creating instances of three balls.
ball_1 = BallBounce(25.0,   25.0,  30.0, -25.0, "dark orange" ) 
ball_2 = BallBounce(475.0,  25.0, -30.0, -25.0, "red")  
ball_3 = BallBounce(475.0, 475.0, -50.0, -15.0, "yellow")  

for i in range(1,2000):       # End the program after 1000 position shifts.  
    ball_1.diffEquation() 
    ball_2.diffEquation() 
    ball_3.diffEquation() 

    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)   # This makes execution pause for 200 milliseconds. 
    canvas_1.delete(ALL)              # This erases everything on the canvas. 

root.mainloop()
