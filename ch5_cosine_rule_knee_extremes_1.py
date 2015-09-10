"""
Program name: cosine_rule_knee_extremes_1.py
Objective: Make cosine rule knee positioner that is immune to critical angle transitions.
Prove coding for calculation of knee position, given foot and hip positions 
as well as thigh and calf length.

Keywords: canvas, cosine rule, knee position.
============================================================================79 
Comments: The critical angles occur when cosine(theta) = 1. 
We avoid this by adjusting the thy_len constant temporarily before the cosine is evaluated.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
import math
import time
root = Tk()
root.title("Move Cosine Rule through Critical Values") 

cw = 600                                      # canvas width
ch = 480                                      # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 200 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    chart_1.delete('line_1')           # This erases everything on the canvas.

#=======================================================================

def knee_position(x_hip, y_hip, x_foot, y_foot, thy_len, calf_len):
    """ Calculate the absolute position of the knee given foot and hip positions
        as well as thigh and calf lengths.
    """
    x_ca = x_foot - x_hip # The sign (sense) of this vector does not alter the rtesult.
    y_ca = y_foot - y_hip
    len_ca = math.sqrt(x_ca * x_ca + y_ca * y_ca)  # Foot-hip distance.
    # Ensure sum of thigh and calf length do not exceed foot to hip distamce.
    thy_calf_ratio = thy_len/calf_len
    straight_leg  = thy_len + calf_len
    if straight_leg <= len_ca:
        straight_leg = len_ca * 1.0001 # Force calf-thigh sum to be 0.01% longer than leg length.
        thy_len = thy_calf_ratio * straight_leg/2
        calf_len = straight_leg - thy_len
    cosine_c = (calf_len*calf_len + len_ca*len_ca - thy_len*thy_len)/(2*calf_len*len_ca)
    #-----------------------------------------------------------
    # Must the knee point forwards (mammalian) or backwards (avian)?
    #rads_c = math.acos(cosine_c)                           # Mamallian knee.
    #theta_2 = math.atan2( (y_foot-y_hip), (x_foot-x_hip))  # Mamallian knee.
    rads_c = math.acos(-cosine_c)                               # Gives backwards-bend knee.
    theta_2 = math.atan2( (y_hip - y_foot ), (x_hip - x_foot )) # Gives backwards-bend knee.
    #-----------------------------------------------------------
    theta_1 = theta_2 + rads_c
    x_b = x_foot - calf_len * math.cos(theta_1)
    y_b = y_foot - calf_len * math.sin(theta_1)
    return  x_b, y_b

#======================================================================
def test_knee_pos(x_hip, y_hip, x_foot, y_foot, thy_len, calf_len):

    x_b, y_b = knee_position(x_hip, y_hip, x_foot, y_foot, thy_len, calf_len)
    chart_1.create_line(x_hip, y_hip, x_foot, y_foot, fill="black", width = 2, tag = 'line_1') 
    chart_1.create_line(x_hip, y_hip,  x_b, y_b, fill="blue", width = 1, tag = 'line_1') 
    chart_1.create_line(x_b, y_b, x_foot, y_foot, fill="red", width = 1, tag = 'line_1') 
    animdelay()

# 3 knee_position(x_hip, y_hip, x_foot, y_foot, thy_len, calf_len)
x_hip = 100.0
y_hip = 200.0
x_foot = 500.0
y_foot = 200.0
thy_len = 202.0
calf_len = 202.0

for i in range(50):
    test_knee_pos(x_hip, y_hip, x_foot, y_foot, thy_len, calf_len)
    thy_len -= 0.5

    print 'thy_len: ', thy_len
    print 'calf_len: ', calf_len
    print '..........................'

root.mainloop()
