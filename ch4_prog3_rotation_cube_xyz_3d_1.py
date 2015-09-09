"""
Program name: rotation cube_xyz_3d_1.py
Objective: Rotate a cube specified by its 3D cartesian coordinates,
around the x, y or z axis.

Keywords: canvas, cube, rotation, 3 dimension, 3d, poition vector
============================================================================79
Comment: This method uses trigonometric projections without the benefit
of the matrix transforms of linear algebra.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python version 3..2 or higher.
import time
root = Tk()
root.title("Rotate a cube in 3D.")
import math

cw = 900                                      # canvas width
ch = 800                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)
cycle_period = 30    # time between new positions of the ball (milliseconds).
#===========================================================================
# The Rotation Funxtions. Each function rotates a 3D point (x,y,z) around one
# of the three reference axes X or Y or Z. The output (return value)
# is a similar point (xx,yy,zz) resulting from the rotation.
def rotate_on_x(xyz, phi_x):
    """ Rotate a position vector around the X-axis. by phi_x degrees.
    """
    A = math.sqrt(xyz[1]*xyz[1] + xyz[2]*xyz[2])  
    alpha = math.atan2(xyz[1], xyz[2])
    xx = xyz[0]
    yy = A   * math.sin(alpha + phi_x)
    zz = A   * math.cos(alpha + phi_x)
    return [xx, yy, zz]

def rotate_on_y(xyz, phi_y):
    """ Rotate a position vector around the Y-axis. by phi_y degrees.
    """

    D = math.sqrt(xyz[0]*xyz[0] + xyz[2]*xyz[2])
    gamma = math.atan2(xyz[2], xyz[0])
    xx = D * math.cos(gamma + phi_y)
    yy = xyz[1]
    zz = D * math.sin(gamma + phi_y)
    return [xx, yy, zz]

def rotate_on_z(xyz, phi_z):
    """ Rotate a position vector around the Z-axis. by phi_z degrees.
    """
    B = math.sqrt(xyz[0]*xyz[0] + xyz[1]*xyz[1])
    beta = math.atan2(xyz[0], xyz[1])
    xx = B * math.sin(beta + phi_z)
    yy = B * math.cos(beta + phi_z)
    zz = xyz[2]
    return [xx, yy, zz]

#=====================================================================
# The shift and amplify functions below adjust only the x and y components
# of the position vectors so that they will appear at a convenient viewing
# position on the drawing canvas. The 3D nature of the position vectors is
# preserved in the input arguments as well as in the return outputs.

def shift(x_shf, y_shf, xyz):
     """ Translate or shift the point xx, yy to the point xx+xx_shf, yy+yy_shf.
     """
     xx_temp = xyz[0] + x_shf
     yy_temp = xyz[1] + y_shf 
     zz = xyz[2]
     return [ xx_temp, yy_temp, zz ]

def amplify(x_scale, y_scale, xyz):
     """ Amplify or scale the point xx, yy to the point xx*x_scale, yy*y_scale.
     """
     xx_temp = xyz[0] * x_scale
     yy_temp = xyz[1] * y_scale
     zz = xyz[2]
     return [ xx_temp, yy_temp, zz ]

#=======================================================================
def pointsetup(xyz_point, x_scale, y_scale, x_shf, y_shf):
    """ Initialize the points for plotting. This ensures the graphic images
        start cleanly from a well defined convenient viewing position.
    """  
    xyz = amplify(x_scale, y_scale, xyz_point)    # Scale the points up or down.
    xyz = shift(x_shf, y_shf, xyz)                # Shift to a convenient viewing position.
    return xyz

x_scale, y_scale = 2., 2.
x_shf, y_shf = 100, 100
phi_x, phi_y, phi_z = 0., 0., 0. # Rotation angles around the major axes. 

xyz_1 = [-100,   100, 100 ]
xyz_2 = [ 100,   100, 100 ]
xyz_3 = [ 100,  -100, 100 ]
xyz_4 = [-100,  -100, 100 ]

xyz_5 = [-100,  100, -100 ]
xyz_6 = [ 100,  100, -100 ]
xyz_7 = [ 100, -100, -100 ]
xyz_8 = [-100, -100, -100 ]

cube_1 = [ xyz_1, xyz_2, xyz_3, xyz_4, xyz_5, xyz_6, xyz_7, xyz_8 ] 

x_scale, y_scale = 2., 2.
x_shf, y_shf = 450, 350

xyz_temp = []
for i in range (len(cube_1)):
    xyz = pointsetup(cube_1[i], x_scale, y_scale, x_shf, y_shf) 
    xyz_temp.append(xyz)


for i in range(1,10000):       # end the program after 500 position shifts.
    phi_x += 0.02
    phi_y += 0.005
    phi_z += 0.001
    
    for i in range(len(cube_1)):
        xyz = rotate_on_x(cube_1[i], phi_x)    # Rotate around x.
        xyz = rotate_on_y(xyz, phi_y)          # Rotate around y.
        xyz = rotate_on_z(xyz, phi_z)          # Rotate around z.    
        xyz = amplify(x_scale, y_scale, xyz)   # Scale the points up or down.
        xyz = shift(x_shf, y_shf, xyz)         #Shift (aka translate).
        chart_1.create_line(xyz[0], xyz[1],  xyz_temp[i][0], xyz_temp[i][1], fill='#990000')
        chart_1.create_line(xyz[0], xyz[1],  xyz_temp[i][0], xyz_temp[i][1], tag = 'line_1', width= 4, fill='#dddd00')
        xyz_temp[i] = xyz
    
    front_rectangle = [xyz_temp[0][0],xyz_temp[0][1], 
                       xyz_temp[1][0],xyz_temp[1][1], 
                       xyz_temp[2][0],xyz_temp[2][1], 
                       xyz_temp[3][0],xyz_temp[3][1], 
                       xyz_temp[0][0],xyz_temp[0][1], ]
    chart_1.create_line(front_rectangle, tag = 'line_1', width= 4, fill='#dddd00')

    back_rectangle  = [xyz_temp[4][0],xyz_temp[4][1], 
                       xyz_temp[5][0],xyz_temp[5][1], 
                       xyz_temp[6][0],xyz_temp[6][1], 
                       xyz_temp[7][0],xyz_temp[7][1], 
                       xyz_temp[4][0],xyz_temp[4][1], ]
    chart_1.create_line(back_rectangle, tag = 'line_1', width= 4, fill='#44dd00')
    
    edge_04 = [xyz_temp[0][0],xyz_temp[0][1],xyz_temp[4][0],xyz_temp[4][1],]
    chart_1.create_line(edge_04, tag = 'line_1', width= 4, fill='#0044dd')

    edge_15 = [xyz_temp[1][0],xyz_temp[1][1],xyz_temp[5][0],xyz_temp[5][1],]
    chart_1.create_line(edge_15, tag = 'line_1', width= 4, fill='#0044dd')

    edge_26 = [xyz_temp[2][0],xyz_temp[2][1],xyz_temp[6][0],xyz_temp[6][1],]
    chart_1.create_line(edge_26, tag = 'line_1', width= 4, fill='#0044dd')

    edge_37 = [xyz_temp[3][0],xyz_temp[3][1],xyz_temp[7][0],xyz_temp[7][1],]
    chart_1.create_line(edge_37, tag = 'line_1', width= 4, fill='#0044dd')

    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.        
    chart_1.delete('line_1')
root.mainloop()
