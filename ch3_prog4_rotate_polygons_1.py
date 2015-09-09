""" 
Program name: rotate_polygons_1 .py 
Objective: Rotate a group of complex polygons. 

Keywords: polygon groups, rotate,  
============================================================================79 
Comment: Rotating a group of complex and detailed lines is very similar
to rotating a single line.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python version 3.2 and higher.
import math 
root = Tk() 
root.title("Rotating Polygon Group") 

cw = 600                                      # canvas width 
ch = 600                                      # canvas height 
chart_1 = Canvas(root, width=cw, height=ch, background="white") 
chart_1.grid(row=0, column=0) 

#=======================================================================================
# A multi-line drawing of a cat.
kitty =  [[-120, 135, -137, 92, -111, 39, -115, -16, -129, -78, -125, -134, -86, -90, -48, -59, -9, -68, 13, -69, 49, -68, 82, -86, 116, -122, 102, -43, 122, -5, 137, 45, 124, 100],
[13, 110, 0, 121, 0, 143, 23, 154, 57, 148, 86, 129, 101, 140, 116, 139, 125, 123, 122, 102, 117, 91],
[85, 127, 87, 115, 79, 111, 70, 99, 61, 97, 65, 86, 85, 90, 105, 84, 108, 93, 99, 97, 94, 111, 89, 114],
[102, 149, 96, 160, 81, 167, 58, 167, 43, 161],
[28, 37, 16, 34, -2, 41, -18, 39, -27, 32, -34, 21, -45, 21, -27, 10, -4, 4, 14, 10, 27, 34, 27, 34],
[-4, 34, 0, 27, 1, 20, -2, 15, -1, 11, 2, 10, 9, 12, 15, 19, 13, 26, 7, 33, -2, 36, -12, 35, -21, 29, -25, 23, -26, 16, -20, 12, -10, 10, -10, 12, -11, 18, -9, 27, -6, 33], [82, 12, 88, 2, 100, -3, 112, -2, 120, 2, 119, 8, 115, 21, 107, 28, 98, 32, 85, 29, 81, 25, 81, 18, 81, 15],
[102, 22, 104, 14, 105, 8, 102, 7, 101, 5, 104, 3, 109, 3, 114, 4, 114, 11, 110, 20, 104, 24, 98, 27, 89, 25, 82, 24, 81, 18, 84, 12, 89, 8, 94, 5, 94, 8, 94, 13, 97, 20, 100, 24],
[89, 172, 94, 205],
[114, -12, 103, -11, 91, -7, 82, 1, 79, 13, 78, 24, 82, 36, 88, 50, 96, 64],
[-58, 15, -45, 4, -29, -6, -11, -9, 10, -1, 27, 14, 37, 30, 43, 46]]
#=======================================================================================
cycle_period = 50 # pause duration (milliseconds). 
def animation_pause_redraw(): 
    chart_1.update()              
    chart_1.after(cycle_period)    
    chart_1.delete('line_1') 

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

for MOVIE in range(0, 700): 
    for FRAME in range(len(kitty)):
       polygon_xy = [] 
       for SHAPE in range(0, len(kitty[FRAME]), 2):           
          xy = cart2polar( kitty[FRAME][SHAPE],  kitty[FRAME][SHAPE+1],  angle) 
          xy_x =  xy[0] 
          xy_y =  xy[1] 
          polygon_xy.append(xy_x) 
          polygon_xy.append(xy_y) 
       angle += 0.002 
       chart_1.create_line(polygon_xy,  width = 3, fill='green', tag='line_1') 
    animation_pause_redraw()           

root.mainloop()
