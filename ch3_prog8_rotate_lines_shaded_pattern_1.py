"""
Program name: rotate_lines_shaded_pattern_1.py
Objective: Rotate four lines, tip to tip.
Show the locus of the tip as a trail.

Keywords: canvas, line, rotation, time, movement, tip locus
============================================================================79
 
Explanation: Establish facility with the trigonometry of the requirements.
angles are expressed both in degrees and radians. The degrees manifestation
is redundant.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine

"""
from Tkinter import *
import time
import math
root = Tk()

cw = 600                                      # canvas width
ch = 600                                      # canvas height

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 50 # time between new positions of the ball (milliseconds).

p1_x = 250.0
p1_y = 250.0

p2_x = 300.0
p2_y = 300.0

p3_x = 150.0
p3_y = 150.0

p4_x = 140.0
p4_y = 140.0


a_radian_1 = math.atan((p2_y - p1_y)/(p2_x - p1_x))
a_length_1 = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +  (p2_x - p1_x)*(p2_x - p1_x))
a_degree_1 = a_radian_1 * 180.0 / math.pi
a_radian_2 = math.atan((p1_y - p3_y)/(p1_x - p3_x))
a_length_2 = math.sqrt((p3_y - p1_y)*(p3_y - p1_y) +  (p3_x - p1_x)*(p3_x - p1_x))
a_degree_2 = a_radian_2 * 180.0 / math.pi
a_radian_3 = math.atan((p3_y - p4_y)/(p3_x - p4_x))
a_length_3 = math.sqrt((p4_y - p3_y)*(p4_y - p3_y) +  (p4_x - p3_x)*(p4_x - p3_x))
a_degree_3 = a_radian_3 * 180.0 / math.pi

trail_x = 150.0
trail_y = 150.0

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

"""
 # this is the magic rgb-to-hex function.
   def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
   # for example:
    rgb_to_hex((255, 255, 255))       #==> '#ffffff'
    rgb_to_hex((65535, 65535, 65535)) #==> '#ffffffffffff'
"""
red_1 = 20
green_1 = 20
blue_1 = 20

# This loop alters the color.
for j in range (1,10):  # 

    a_length_1 -= 3

    if 5 < blue_1 or blue_1 < 250:
        blue_1 += 2
    else:
        blue_1 = 0

    if 25 < red_1 or red_1 < 230:
        red_1 += 24
    else:
        red_1 = 10
    a_degree_1 +=3.0
    a_radian_1 = a_degree_1 * math.pi / 180

    color_A = (red_1, green_1, blue_1)
    print 'color_A: ', color_A
    color_B = rgb_to_hex(color_A)


    # This loop alters line positions.
    for i in range(1,13):       # end the program after 100x130 position shifts.


        a_degree_1 +=3.0
        a_radian_1 = a_degree_1 * math.pi / 180
        a_degree_2 +=12.0
        a_radian_2 = a_degree_2 * math.pi / 180
        a_degree_3 -=6.0
        a_radian_3 = a_degree_3 * math.pi / 180

        p1_x = p2_x - a_length_1 * math.cos(a_radian_1)
        p1_y = p2_y - a_length_1 * math.sin(a_radian_1)

        trail_x3 = p3_x
        trail_y3 = p3_y
        p3_x = p1_x - a_length_2 * math.cos(a_radian_2)
        p3_y = p1_y - a_length_2 * math.sin(a_radian_2)
        chart_1.create_line(trail_x3, trail_y3, p3_x, p3_y, width=1, fill=color_B)
    
        trail_x4 = p4_x
        trail_y4 = p4_y
        p4_x = p3_x - a_length_3 * math.cos(a_radian_3)
        p4_y = p3_y - a_length_3 * math.sin(a_radian_3)
        chart_1.create_line(trail_x4, trail_y4, p4_x, p4_y, width=1, fill=color_B)

        chart_1.create_line(p1_x, p1_y, p2_x, p2_y, tag='line_1', fill='#202020')
        chart_1.create_line(p1_x, p1_y, p3_x, p3_y, tag='line_2', fill='#202020')
        chart_1.create_line(p3_x, p3_y, p4_x, p4_y, tag='line_3', fill='#444455')

        chart_1.update()              # This refreshes the drawing on the canvas.
        chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
        chart_1.delete('line_1', 'line_2', 'line_3')           # This erases everything on the

root.mainloop()
