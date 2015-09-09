""" 
Program name: rotate_rough_head_3d_1.py 
Objective: Rotate about the y-axis, a list of points representing some features on a crude face. 
around the X, Y or Z axis. 

Keywords: canvas, line, rotation, 3 dimension, 3d, face features.
============================================================================79 
Comment: This method uses trigonometric projections without the benefit 
of the matrix transforms of linear algebra. 

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine 
""" 
#from Tkinter import * 
from tkinter import *  # For Python version 3.2 and higher. 
import time 
root = Tk() 
root.title("Rough rotating head 3D.") 
import math 

cw = 500                                      # canvas width 
ch = 400                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=0) 
cycle_period = 300    # time between new positions of the ball (milliseconds). 

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
    return [xx, yy, zz] 

def rotate_on_x(xyz, phi_x): 
    """ Rotate a position vector around the X-axis. by phi_x degrees. 
       Input arguments are (x,y,z)vector and phi_x, angle of ratation about x.
    """ 
    A = math.sqrt(xyz[1]*xyz[1] + xyz[2]*xyz[2])  
    alpha = math.atan2(xyz[1], xyz[2]) 
    xx = xyz[0] 
    yy = A   * math.sin(alpha + phi_x) 
    zz = A   * math.cos(alpha + phi_x) 
    return [xx, yy, zz] 

def rotate_on_y(xyz, phi_y): 
    """ Rotate a position vector around the Y-axis. by phi_y degrees.
        Input arguments are (x,y,z)vector and phi_y, angle of ratation about y. 
    """ 
    D = math.sqrt(xyz[0]*xyz[0] + xyz[2]*xyz[2]) 
    gamma = math.atan2(xyz[2], xyz[0]) 
    xx = D * math.cos(gamma + phi_y) 
    yy = xyz[1] 
    zz = D * math.sin(gamma + phi_y) 
    return [xx, yy, zz] 

def rotate_on_z(xyz, phi_z): 
    """ Rotate a position vector around the Z-axis. by phi_z degrees.    
       Input arguments are (x,y,z)vector and phi_z, angle of ratation about x. 
    """ 
    B = math.sqrt(xyz[0]*xyz[0] + xyz[1]*xyz[1]) 
    beta = math.atan2(xyz[0], xyz[1]) 
    xx = B * math.sin(beta + phi_z) 
    yy = B * math.cos(beta + phi_z) 
    zz = xyz[2] 
    return [xx, yy, zz] 

def shift(x_shift, y_shift, xyz): 
     """ Translate or shift the point xx, yy to the point xx+xx_shift, yy+yy_shift. 

     """ 
     xx_temp = xyz[0] + x_shift 
     yy_temp = xyz[1] + y_shift 
     zz = xyz[2] 
     return [ xx_temp, yy_temp, zz ] 

def amplify(x_scale, y_scale, xyz): 
     """ Amplify or scale the point xx, yy to the point xx*x_scale, yy*y_scale. 
     """ 
     xx_temp = xyz[0] * x_scale 
     yy_temp = xyz[1] * y_scale 
     zz = xyz[2] 
     return [ xx_temp, yy_temp, zz ] 


#===============================================
# The shape of the facial features.
l_ear = [[-26.5, 0, 2.1],  [-30,0,-2.1], [-31.5,-3,-0.8], [-28,-17,-5.4], [-25.3,-18,-5.7]]
r_ear = [[26.5, 0, 2.1],  [30,0,-2.1], [31.5,-3,-0.8], [28,-17,-5.4], [25.3,-18,-5.7]]
l_nose = [ [0, -4.8, -23], [-3.5, -17.2, -23 ], [0, -17.3, -33 ] ]
r_nose = [  [0, -17.3, -33 ],    [3.5, -17.2, -23 ], [0, -4.8, -23]  ]
mouth = [[-7.4, -22.1,-20],[-4.6,-24.2,-22],[-1.1,-24.8,-22],[0,-24.8,-22],  [1.1,-24.8,-26],[4.6,-24.2,-22],[7.4, -22.1,-20]  ]
l_eye = [[-14.4,-1.7,-22.6],[ -13.9,-0.7,-22.3],[-12.7, -0.1, -22.4],[ -11.5,-0.3,-22.2], [-10.7, -1.3, -22.6],  [-11.1, -2.5, -22.9], [-12.3, -3, -23.0],[-13.4,-2.8,-23.0]]
r_eye = [[14.4,-1.7,-22.6], [ 13.9,-0.7,-22.3],[12.7, -0.1, -22.4],  [ 11.5,-0.3,-22.2],  [10.7, -1.3, -22.6],   [11.1, -2.5, -22.9], [12.3, -3, -23.0],[13.4,-2.8,-23.0]]
face = [[0,40.2,0], [-15.5,36.3,0],[-23.6, 30.0,0],[-27.1, 22.1, 0],[-26.1,14.3,0],[-23.5,-25,0],[-14.5,-33.8, 0],[-4.4, -38.8,0], [0,-39.7,0],  [4.4, -38.8,0],[14.5,-33.8, 0],[23.5,-25,0],[26.1,14.3,0],[27.1, 22.1, 0],[23.6, 30.0,0], [15.5,36.3,0], [0,40.2,0]]

kula_mouth = '#990000'
kula_nose  = '#999900'
kula_eye  = '#000000'
kula_ear  = '#aaaa00'

x_scale, y_scale = 3.8, -3.8 
x_shift, y_shift = 250, 200 
deg1   = math.pi/ 180.  # radians = 1 degree 
deg10  = 10*deg1 
deg5 = 5*deg1 
delta_phi = deg5/72 
radius, theta, phi = 100., 0., 0. 


#Draw face outline - a static background.
xy_new = [] 
for i in range(0, len(face)):
    face[i] =  amplify(x_scale, y_scale, face[i])   # Amplify the spiral.
    face[i] =  shift(x_shift, y_shift, face[i])              # Shift sideways and down. 
    x = face[i][0]
    xy_new.append(x)
    y = face[i][1]
    xy_new.append(y)

canvas_1.create_polygon( xy_new, width= 3, fill='#aaaa00') 


phi_x, phi_y, phi_z = 0., 0., 0. # Rotate the spiral around X and Y axes. 

def rotate_feature(feature_shape, x_scale, y_scale, x_shift, y_shift, phi_y):
    """ Rotate a feature around the y-axis.
    """
    xy_rotated_feature = []

    for j in range(len(feature)): 
            xyz_feature = feature[j][0], feature[j][1], feature[j][2]      
            new_feature = rotate_on_y(xyz_feature, phi_y) 

            new_feature = amplify(x_scale, y_scale, new_feature)   # Amplify the spiral. 
            new_feature = shift(x_shift, y_shift, new_feature)              # Shift sideways and down. 
            xx = new_feature[0] 
            yy = new_feature[1] 
            xy_new_feature.append(xx) 
            xy_new_feature.append(yy)  


# A function to assemble the features of a crude cartoon face from a shape (the facial feature).
def assemble_3d_face_feature_(feature_xyz, x_scale, y_scale, x_shift, y_shift, kula, phi):
     """ rotate and sssemble, for display, a facial feature, expressed as a 3d coordinate list, 
     input arguments are the feature, it's color, and the size and shift values to convenient
     placement on the canvas.
     """
     xy_new_feature = []
     for j in range(len(feature_xyz)): 
            xyz_feature = feature_xyz[j][0], feature_xyz[j][1], feature_xyz[j][2]      
            new_feature = rotate_on_y(xyz_feature, phi_y) 
            new_feature = amplify(x_scale, y_scale, new_feature)   # Amplify the spiral. 
            new_feature = shift(x_shift, y_shift, new_feature)              # Shift sideways and down. 
            xx = new_feature[0] 
            yy = new_feature[1] 
            xy_new_feature.append(xx) 
            xy_new_feature.append(yy)  
     canvas_1.create_polygon( xy_new_feature, width= 4, tag='line_1', fill=kula) 


for k in range( 2000): 

        assemble_3d_face_feature_(mouth,  x_scale, y_scale, x_shift, y_shift, kula_mouth, phi_y) 
        assemble_3d_face_feature_(l_nose, x_scale, y_scale, x_shift, y_shift, kula_nose, phi_y) 
        assemble_3d_face_feature_(r_nose, x_scale, y_scale, x_shift, y_shift, kula_nose, phi_y) 
        assemble_3d_face_feature_(l_eye,  x_scale, y_scale, x_shift, y_shift, kula_eye, phi_y) 
        assemble_3d_face_feature_(r_eye,  x_scale, y_scale, x_shift, y_shift, kula_eye, phi_y) 
        assemble_3d_face_feature_(l_ear,  x_scale, y_scale, x_shift, y_shift, kula_ear, phi_y) 
        assemble_3d_face_feature_(r_ear,  x_scale, y_scale, x_shift, y_shift, kula_ear, phi_y) 

        phi_y += 10.*deg1 
        canvas_1.update()              # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)   # This makes execution pause for 50 milliseconds.        
        canvas_1.delete('line_1') 

root.mainloop() 
