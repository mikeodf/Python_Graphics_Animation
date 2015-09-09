"""
Program name: rotate_spiral_3d_1.py
Objective: Rotate a list of points specified by their 3D cartesian coordinates,
around the X, Y or Z axis.

Keywords: canvas, line, rotation, 3 dimension, 3d, poition vector
============================================================================79
Comment: This method uses trigonometric projections without the benefit
of the matrix transforms of linear algebra.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import time
root = Tk()
root.title("Rotate a cube in 3D.")
import math

cw = 850                                      # canvas width
ch = 800                                      # canvas height

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

cycle_period = 30    # time between new positions of the ball (milliseconds).

# 3D Cartesian to Polar coordinates.
def cart2polar(xyz):
    """ Convert Cartesian rectangular coordinates [x,y,z] to polar coordinates
        [Length, alfa, beta ] where alfa is the angle in x-z plane, from X axis),
        and beta is the smallest angle to Length from Y-axis. 
    """  
    len1 = math.sqrt(xyz[0]*xyz[0] +xyz[2]*xyz[2])
    theta = math.atan2(xyz[0], xyz[2])
    phi = math.atan2(xyz[1], len1)
    Radius = math.sqrt(xyz[0]*xyz[0]  + xyz[1]*xyz[1] + xyz[2]*xyz[2])
    return [Radius, theta, phi]

# 3D Polar coordinates to Cartesian.
def polar2cart(Rtp):
    """ Convert Angular coordinates intoCartesian rectangular coordinates
        Rtp = [Radius, theta, phi ].  Where angle in x-z plane, from Z axis,
        and phi is the smallest angle to Radius from Y-axis. 
    """ 
    Radius = Rtp[0]
    theta = Rtp[1]
    phi = Rtp[2]
    xx = Radius * math.sin(phi) * math.sin(theta)
    yy = Radius * math.cos(phi) 
    zz = Radius * math.sin(phi) * math.cos(theta)
    #print 'phi: ', phi, '  yy: ', yy
    return [xx, yy, zz]

'''
# Test code for polar2cart and cart2polar to 

radius, theta, phi = 100., 0., 0.
for i in range(6):
    phi +=0.1
    rtp = [ radius, theta, phi ]
    #print 'phi:',phi, '  rtp: ', rtp
    xyz = polar2cart(rtp)
    print 'xyz: ', xyz
    RTP = cart2polar(xyz)
    print 'RTP: ', RTP
    xyz = polar2cart(rtp)
    print 'xyz: ', xyz
'''
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

def pointsetup(xyz, phi,x_scale,y_scale, x_shf, y_shf):
    """ Initialize the points for plotting.
        That is, amplify and shift them for convenient viewing.
    """
    xyz = rotate_on_x(xyz, phi_x)   # Rotate around z.   
    xy_amp = amplify(x_scale, y_scale, xyz)    # Scale the points up pr down.
    xy_shf = shift(x_shf, y_shf, xy_amp)    # Rotate around x.
    return xyz

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
'''
# Coordinates for the corners of a cube.
xyz_1 = [-100,   100, 100 ]
xyz_2 = [ 100,   100, 100 ]
xyz_3 = [ 100,  -100, 100 ]
xyz_4 = [-100,  -100, 100 ]

xyz_5 = [-100,  100, -100 ]
xyz_6 = [ 100,  100, -100 ]
xyz_7 = [ 100, -100, -100 ]
xyz_8 = [-100, -100, -100 ]

cube_1 = [ xyz_1, xyz_2, xyz_3, xyz_4, xyz_5, xyz_6, xyz_7, xyz_8 ] 
'''
x_scale, y_scale = 2., 2.
x_shf, y_shf = 450, 400
Radius,theta, phi = 100., 0., 0.    # Polar coordinates. 
rtp = [Radius, theta, phi]

def pointsetup(xyz_point, x_scale, y_scale, x_shf, y_shf):
    """ Initialize thr points for plotting. This ensures the graphic images
        start cleanly.
    """  
    xyz = amplify(x_scale, y_scale, xyz_point)  # Scale the points up pr down.
    xyz = shift(x_shf, y_shf, xyz)              # Shift to a convenient viewing position.
    return xyz
''' 
# Set up initial values.
xyz_temp = []
for i in range (len(cube_1)):
    xyz = pointsetup(cube_1[i], x_scale, y_scale, x_shf, y_shf) 
    xyz_temp.append(xyz)
'''
rtp = 100., 0., 0.
#xyz = polar2cart(rtp)
# Standard angles
deg1  =math.pi/ 180.  # radians = 1 degree
deg2  = 2. * deg1     # radians = 2 degree
deg5  = 5. * deg1     # radians = 5 degree
deg10 = 10. * deg1    # radians = 10 degree
deg20 = 20 * deg1
rtp = 100., 0., 0.
#xyz_old = polar2cart(rtp)
radius, theta, phi = 100., 0., 0.
theta = 0.
phi = 0.
del_phi = deg5/9

# Make an instance of the spherical spiral. 
spiral = []
for j in range(18):     # 18x9 = 162 points
    for i in range(9):
        theta += deg20
        phi +=del_phi       
        rtp = [ radius, theta, phi ]
        xyz = polar2cart(rtp)
        xx = xyz[0]
        yy = xyz[1]
        zz = xyz[2]
        spiral.append(xx)  
        spiral.append(yy)  
        spiral.append(zz)  

print 'len(spiral): ', len(spiral)
# Rotate the spiral around y
phi_y = 0.
xy_new = []
for k in range( 200):

    for i in range(0, len(spiral),3):
        xyz = spiral[i], spiral[i+1], spiral[i+2]
        xyz = rotate_on_y(xyz, phi_y)
        #xyz = rotate_on_x(xyz, phi_y)
        #xyz = rotate_on_z(xyz, phi_y)
        xyz = amplify(x_scale, y_scale, xyz)   # Scale the points up or down.
        xyz = shift(x_shf, y_shf, xyz) 
        xx = xyz[0]
        yy = xyz[1]
        xy_new.append(xx)
        xy_new.append(yy)  
    phi_y += deg1
    chart_1.create_line( xy_new, width= 3, tag='line_1', fill='#990000')
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.        
    chart_1.delete('line_1')
    xy_new = []

print 'len(xy_new): ', len(xy_new)

root.mainloop()

