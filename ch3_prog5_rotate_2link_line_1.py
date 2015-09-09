""" 
Program name: rotate_2link_line_1.py 
Objective: Rotate two lines, one at the tip of the other. 
Show the locus of the tip as a trail. 

Keywords: canvas, line, rotation, time, movement, tip locus 
===================================================================79 
Comments: Establish facility with the trigonometry of the requirements. 
angles are expressed both in degrees and radians. The degrees manifestation 
is redundant. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine 

""" 
from Tkinter import * 
import time 
import math 
root = Tk() 
root.title('Four leaf clover.') 

cw = 600                                     # canvas width 
ch = 600                                      # canvas height 

chart_1 = Canvas(root, width=cw, height=ch, background="black") 
chart_1.grid(row=0, column=0) 

cycle_period = 50 # time between new positions of the ball (milliseconds). 
alpha_deg =  10.0 
alpha_inc = 5.0 

p1_x = 200.0 
p1_y = 200.0 
v1_x = 100.0 
v1_y = 100.0 

p2_x = 300.0 
p2_y = 300.0 
v2_x = 200.0 
v2_y = 200.0 

p3_x = 150.0 
p3_y = 150.0 
v3_x = 100.0 
v3_y = 100.0 

a_radian_1 = math.atan((p2_y - p1_y)/(p2_x - p1_x)) 
a_length_1 = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +  (p2_x - p1_x)*(p2_x - p1_x)) 
a_degree_1 = a_radian_1 * 180.0 / math.pi 
a_radian_2 = math.atan((p1_y - p3_y)/(p1_x - p3_x)) 
a_length_2 = math.sqrt((p3_y - p1_y)*(p3_y - p1_y) +  (p3_x - p1_x)*(p3_x - p1_x)) 
a_degree_2 = a_radian_2 * 180.0 / math.pi 

trail_x = 150.0 
trail_y = 150.0 

for i in range(1,5000):       # end the program after 500 position shifts. 


    a_degree_1 +=1.5 
    a_radian_1 = a_degree_1 * math.pi / 180 
    a_degree_2 +=3.5 
    a_radian_2 = a_degree_2 * math.pi / 180 

    p1_x = p2_x - a_length_1 * math.cos(a_radian_1) 
    p1_y = p2_y - a_length_1 * math.sin(a_radian_1) 
    trail_x = p3_x 
    trail_y = p3_y 

    p3_x = p1_x - a_length_2 * math.cos(a_radian_2) 
    p3_y = p1_y - a_length_2 * math.sin(a_radian_2) 
    chart_1.create_line(trail_x, trail_y, p3_x, p3_y, width=4, fill='green') 

    chart_1.create_line(p1_x, p1_y, p2_x, p2_y, tag='line_1', fill='dark gray') 
    chart_1.create_line(p1_x, p1_y, p3_x, p3_y, tag='line_2', fill='dark gray') 

    chart_1.update()                              # Refreshes the drawing on the canvas. 
    chart_1.after(cycle_period)            # Make execution pause for 200 milliseconds. 
    chart_1.delete('line_1', 'line_2')      # Erases everything on the canvas.

root.mainloop() 
