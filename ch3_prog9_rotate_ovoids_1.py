"""
Program name: rotate_ovoids_1 .py
Objective: Rotate oviods.

Keywords: canvas, line, rotate, time, movement
============================================================================79
recipe # 9 
Explanation: Establish facility with the trigonometry of the requirements.

Tested on: Python 2.6,  Python 2.7.3, Python 3.2 
Author:          Mike Ohlson de Fine

"""
# rotate_line_1.py
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from Tkinter import *
import math
import copy

root = Tk()
root.title("Rotating ovoid")

cw = 400                                      # canvas width
ch = 400                                      # canvas height
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 50 # pause duration (milliseconds).

def animation_pause_redraw():
    chart_1.update()
    chart_1.after(cycle_period)
    chart_1.delete('line_1')
#=============================================================
# 90 degree shift
ninety_rot = math.pi/2
deg2rad = math.pi/180      # Degree to radian conversion.
#--------------------------------------------------------------------
# Rotate a single vector about x, y and z axes
def vector_rotate(x, y, alpha):
    """ rotate takes the 2d cartesian cordinates of a point x, y
    and a rotation angle alpha, returning the x and y after rotation.  
    """
    # alpha - rotate from the x axis
    rxy = math.sqrt(x*x + y*y)      # length of first joint.
    alxy = math.atan2(y, x)
    x = rxy * math.sin(alxy + alpha)
    y = rxy * math.cos(alxy + alpha)
    return x, y
#=============================================================
# Shaded ovoids
#oval_2_x = [170, 265, 500, 749, 823, 750, 500, 263]
#oval_2_y = [350, 521, 588, 512, 348, 187, 111, 179]

crescent_left_x = [196, 210, 300, 397, 498, 601, 698, 790, 804, 802, 779, 700, 601, 499, 401, 302, 219, 197]
crescent_left_y =  [348, 445, 525, 564, 575, 564, 525, 445, 351, 351, 417, 482, 525, 533, 525, 488, 414, 347]

crescent_rite_x = [198, 210, 300, 400, 502, 614, 698, 791, 802, 803, 776, 701, 603, 500, 399, 298, 224, 202]
crescent_rite_y =  [350, 255, 174, 139, 126, 141, 172, 258, 347, 347, 279, 214, 178, 165, 179, 216, 280, 352]

oval_3_x = [194, 222, 300, 400, 500, 600, 700, 782, 804, 781, 699, 598, 497, 399, 299, 221]
oval_3_y = [348, 434, 503, 541, 550, 540, 504, 427, 350, 263, 195, 155, 144, 156, 194, 259]


def normalize_list(some_list):
    ''' Shift entire list to make first element = 0
    '''
    first_element = some_list[0]
    for i in range(0, len(some_list)):
        some_list[i] =  some_list[i] - first_element
    return some_list

def resize_shift_shape(shape_x, shape_y, size_x, size_y, org_x, org_y):
    for i in range(0, len(shape_x)):
       shape_x[i] = shape_x[i] * size_x + org_x
       shape_y[i] = shape_y[i] * size_y + org_y
    return shape_x, shape_y

def transpose_shape(shape_x, shape_y):
    xy_temp = copy.deepcopy(shape_x)
    shape_x = shape_y
    shape_y = xy_temp
    return shape_x, shape_y

def display_shape_x_y(shape_x, shape_y, kula):
    xy = []
    for i in range(0, len(shape_x)):
        xy.append(shape_x[i] )
        xy.append(shape_y[i] )
    #chart_1.create_line(xy, fill='grey')
    chart_1.create_polygon(xy,smooth = TRUE, fill=kula, tag = 'line_1')

def display_shape_xy(shape_xy, kula):
    #chart_1.create_line(xy, fill='grey')
    chart_1.create_polygon(shape_xy,smooth = TRUE, fill=kula, tag = 'line_1')



size_x = 0.3
size_y = 0.4


org_x = 300
org_y = 100

oval = transpose_shape(oval_3_x, oval_3_y)
oval_3_x =  oval[0]
oval_3_y =  oval[1]
oval_3_x = normalize_list(oval_3_x)
oval_3_y = normalize_list(oval_3_y)
oval = resize_shift_shape(oval_3_x, oval_3_y, size_x, size_y, org_x, org_y)
oval_3_x =  oval[0]
oval_3_y =  oval[1]

display_shape_x_y(oval_3_x, oval_3_y, 'grey')

oval = transpose_shape(crescent_left_x, crescent_left_y)
crescent_left_x =  oval[0]
crescent_left_y =  oval[1]
crescent_left_x = normalize_list(crescent_left_x)
crescent_left_y = normalize_list(crescent_left_y)
oval = resize_shift_shape(crescent_left_x, crescent_left_y, size_x, size_y, org_x, org_y)
crescent_left_x =  oval[0]
crescent_left_y  =  oval[1]
display_shape_x_y(crescent_left_x, crescent_left_y, 'blue')

oval = transpose_shape(crescent_rite_x, crescent_rite_y)
crescent_rite_x =  oval[0]
crescent_rite_y =  oval[1]
crescent_rite_x = normalize_list(crescent_rite_x)
crescent_rite_y = normalize_list(crescent_rite_y)
oval = resize_shift_shape(crescent_rite_x, crescent_rite_y, size_x, size_y, org_x, org_y)
crescent_rite_x =  oval[0]
crescent_rite_y  =  oval[1]
display_shape_x_y(crescent_rite_x, crescent_rite_y, 'red')


#========================================================================
#========================================================================
# Rotate a complex shapeabout x, y and z axes
def rotate_tip(org_x, org_y, x, y, angle):

    """ rotate takes the 3d cartesian cordinates of a point x, y, z
    and returns polar coordinates of the point projected onto the cartesian planes.
    global rzy, rxz, ryx, alx, aly, alz is a data structure that is common to xyz2polar() and rotate().
    """
    vect_x = x - org_x
    vect_y = y - org_y

    rxy = math.sqrt(vect_x*vect_x + vect_y*vect_y)   
    ang = math.atan2(vect_y, vect_x)
    x = rxy * math.sin(ang + angle)
    y = rxy * math.cos(ang + angle)
    return x, y

#=============================================================
#=============================================================
#=============================================================
# Arbitrary start vector tip

angle = 0.0

for k in range(0, 170):
    #..............................................
    crescent_r = []
    crescent_l = []
    oval_xy = []

    for i in range(0, len(oval_3_x)): 
        oxy = rotate_tip(org_x, org_y,   oval_3_x[i],  oval_3_y[i],  angle)
        oval_xy.append(org_x + oxy[0])
        oval_xy.append(org_y + oxy[1])
        display_shape_xy(oval_xy, 'grey')

    for i in range(0, len(crescent_left_x)): 
        clxy = rotate_tip(org_x, org_y,   crescent_left_x[i],  crescent_left_y[i],  angle)
        crescent_l.append(org_x + clxy[0])
        crescent_l.append(org_y + clxy[1])
    display_shape_xy(crescent_l, 'blue')

    for i in range(0, len(crescent_rite_x)):
        crxy = rotate_tip(org_x, org_y,   crescent_rite_x[i],  crescent_rite_y[i],  angle)
        crescent_r.append(org_x + crxy[0])
        crescent_r.append(org_y + crxy[1])
    display_shape_xy(crescent_r, 'red')

        #......................................

    angle += 0.05
    animation_pause_redraw()           

#=============================================================
#=============================================================
#=============================================================

root.mainloop()
