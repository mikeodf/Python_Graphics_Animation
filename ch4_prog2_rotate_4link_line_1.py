"""
Program name: rotate_4link_line_1.py
Objective: Rotate a complex shape about the Y-axis.

Keywords: canvas, line, 3D rotation, time, movement, tip locus
============================================================================79
Comments: Demonstrate 'synthetic' 3D generation by altering adjusting
only the x coordinate of a shape.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk()
root.title('3D rotation around vertical')
import time
import math

cw = 600                                      # canvas width
ch = 600                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 50 # time between new positions of the ball (milliseconds).

# Starting position of 4 lines
p0_x, p0_y = 300.0, 300.0
p1_x, p1_y = 200.0, 200.0
p2_x, p2_y = 150.0, 150.0
p3_x, p3_y = 100.0, 100.0
p4_x, p4_y = 50.0, 50.0
p5_x, p5_y = 30.0, 30.0

# Calculate the position and length of each line.
alpha_0 = math.atan((p0_y - p1_y)/(p0_x - p1_x))
length_0_1 = math.sqrt((p0_y - p1_y)*(p0_y - p1_y) +  (p0_x - p1_x)*(p0_x - p1_x))

alpha_1 = math.atan((p1_y - p2_y)/(p1_x - p2_x))
length_1_2 = math.sqrt((p2_y - p1_y)*(p2_y - p1_y) +  (p2_x - p1_x)*(p2_x - p1_x))

alpha_2 = math.atan((p2_y - p3_y)/(p2_x - p3_x))
length_2_3 = math.sqrt((p3_y - p2_y)*(p3_y - p2_y) +  (p3_x - p2_x)*(p3_x - p2_x))

alpha_3 = math.atan((p3_y - p4_y)/(p3_x - p4_x))
length_3_4 = math.sqrt((p4_y - p3_y)*(p4_y - p3_y) +  (p4_x - p3_x)*(p4_x - p3_x))

alpha_4 = math.atan((p3_y - p5_y)/(p3_x - p5_x))
length_4_5 = math.sqrt((p5_y - p4_y)*(p5_y - p4_y) +  (p5_x - p4_x)*(p5_x - p4_x))

b_radian = 0.0
for k in range(1,500):
    ''' Synthetic 3D - Rotation around the y-axis (vertical) by 
        modulating the x-component of each line.
    '''
    len1_x = length_0_1 * math.cos(b_radian)
    len2_x = length_1_2 * math.cos(b_radian)
    len3_x = length_2_3 * math.cos(b_radian)
    len4_x = length_3_4 * math.cos(b_radian)
    len5_x = length_4_5 * math.cos(b_radian)

    b_radian += 0.01    # Progressive 'rotation' angle.

    for i in range(1,630):   # End the program after 630 position shifts.

        alpha_0 += 0.01
        alpha_1 -= 0.02
        alpha_2 += 0.04
        alpha_3 -= 0.06
    
        p1_x = p0_x - len1_x * math.cos(alpha_0)
        p1_y = p0_y - length_0_1 * math.sin(alpha_0)

        tip_locus_2_x = p2_x
        tip_locus_2_y = p2_y
        p2_x = p1_x - len2_x * math.cos(alpha_1)
        p2_y = p1_y - length_1_2 * math.sin(alpha_1)

        tip_locus_3_x = p3_x
        tip_locus_3_y = p3_y
        p3_x = p2_x - len3_x * math.cos(alpha_2)
        p3_y = p2_y - length_2_3 * math.sin(alpha_2)

        tip_locus_4_x = p4_x
        tip_locus_4_y = p4_y
        p4_x = p3_x - len4_x * math.cos(alpha_3)
        p4_y = p3_y - length_3_4 * math.sin(alpha_3)

        tip_locus_5_x = p5_x
        tip_locus_5_y = p5_y
        p5_x = p4_x - len5_x * math.cos(alpha_4)
        p5_y = p4_y - length_4_5 * math.sin(alpha_4)

        chart_1.create_line(p4_x, p4_y, p3_x, p3_y, tag='line_4', fill='#85004b')
        chart_1.create_line(p5_x, p5_y, p4_x, p4_y, tag='line_5', fill='#230672')

        # Locus of line tips
        chart_1.create_line(tip_locus_2_x, tip_locus_2_y, p2_x, p2_y, fill='#cd0074')
        chart_1.create_line(tip_locus_3_x, tip_locus_3_y, p3_x, p3_y, fill='#f7fe00')
        chart_1.create_line(tip_locus_4_x, tip_locus_4_y, p4_x, p4_y, fill='#7608aa')
        chart_1.create_line(tip_locus_5_x, tip_locus_5_y, p5_x, p5_y, fill='#85004b')

    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    chart_1.delete(ALL)           # This erases everything on the

root.mainloop()
