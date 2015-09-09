""" 
Program name: rotate_polygon_1 .py 
Objective: Rotate a complex polygon. 

Keywords: canvas, line, rotate, time, movement 
============================================================================79 
Comment: Rotating a complex and detailed line is very similar to rotating
a simple line.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python version 3.2 and higher.
import math 
root = Tk() 
root.title("Rotating Polygon") 

cw = 600                                      # canvas width 
ch = 600                                      # canvas height 
chart_1 = Canvas(root, width=cw, height=ch, background="white") 
chart_1.grid(row=0, column=0) 

cycle_period = 50 # pause duration (milliseconds). 
def animation_pause_redraw(): 
    chart_1.update()              
    chart_1.after(cycle_period)    
    chart_1.delete('line_1') 

# Coordinates of the polygon to be rotated.
polygon_x =  [-120, -137, -111, -115, -129, -125, -86, -48, -9, 13, 49, 82, 116, 102, 122, 137, 124]
polygon_y =  [135, 92, 39, -16, -78, -134, -90, -59, -68, -69, -68, -86, -122, -43, -5, 45, 100]

# Convert Cartesian to Polar coordinates.
def cart2polar( x, y, angle): 
    """ rotate takes the 2d cartesian cordinates of a point x, y
        and returns polar coordinates of the point projected onto the cartesian planes. 
    """ 
    rxy = math.sqrt(x*x + y*y)   
    ang = math.atan2(y, x) 
    y = rxy * math.sin(ang + angle) 
    x = rxy * math.cos(ang + angle) 
    return x, y 

#============================================================= 
# Test and demonstrate.
angle = 0.0 

for k in range(0, 700): 
    polygon_xy = [] 
    for i in range(0, len(polygon_x)):           
        xy = cart2polar( polygon_x[i],  polygon_y[i],  angle) 
        xy_x =  xy[0] 
        xy_y =  xy[1] 
        polygon_xy.append(xy_x) 
        polygon_xy.append(xy_y) 
    angle += 0.05 

    chart_1.create_line(polygon_xy,  width = 3, fill='green', tag='line_1') 
    animation_pause_redraw()           

root.mainloop()
