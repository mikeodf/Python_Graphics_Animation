""" 
Program name: stick_frog_jump_1.py 
Objective: Animate a five stage stick frog jump. 

Keywords: Path, point, line, shape, intermediate positions, motion. 
==================================================79 
Comments:  
The intermediate positions are calculated by interploating transition positions 
along a path. Sub-divide the straight line path between two shapes, composed of 
multiple lines, into a specified number of equi-spaced steps 

Tested on: Python versions 2.6, 2.7, 3.2 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
import itertools 

root = Tk() 
root.title('Horse Near Side , one full strides.') 
cw = 2000                                      # canvas width. 
ch = 600                                       # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#=================================================== 
#   Digitized coordinates of line vertices for frog stick-figure.     
#=============================================== 
# Frame_1 
body_1 = [271, 967, 233, 908, 136, 919, 8, 998, 25, 1031, 194, 1016, 260, 983] 
a_1 = [139, 965, 110, 1012, 161, 1053] 
b_1 = [17, 1010, 85, 975, 43, 1046] 
c_1 = [219, 1003, 219, 1017, 203, 1046] 
d_1 = [13, 1011, 18, 1014, 16, 1018] 
 
# ------------------------------------------------------------------------ 
# Frame_2 
body_2 = [519, 549, 442, 514, 373, 587, 309, 733, 342, 755, 491, 632, 521, 561] 
a_2 =[394, 581, 384, 641, 365, 744] 
b_2 = [313, 736, 286, 768, 234, 857] 
c_2 = [445, 687, 437, 699, 395, 767] 
d_2 = [338, 753, 322, 796, 286, 870] 

# ------------------------------------------------------------------------ 
# Frame_3 
body_3 = [880, 269, 835, 225, 743, 267, 627, 377, 650, 410, 822, 352, 883, 285] 
a_3 = [738, 283, 708, 315, 809, 295] 
b_3 = [627, 376, 577, 385, 525, 452] 
c_3 = [830, 347, 852, 339, 903, 338] 
d_3 = [659, 413, 638, 459, 567, 484] 

# ------------------------------------------------------------------- 
# Frame_4 
body_4 =  [1300, 270, 1303, 218, 1205, 197, 1047, 217, 1045, 257, 1197, 301, 1291, 275] 
a_4 = [1177, 273, 1212, 329, 1278, 372] 
b_4 = [1070, 220, 999, 234, 948, 280] 
c_4 = [1274, 282, 1290, 303, 1306, 346] 
d_4 = [1052, 261, 1037, 274, 1009, 287] 

# -------------------------------------------------------------------- 
# Frame_5 
body_5 = [1517, 714, 1558, 682, 1508, 594, 1421, 521, 1376, 542, 1426, 658, 1508, 711] 
a_5 = [1428, 663, 1422, 721, 1456, 820] 
b_5 = [1384, 549, 1338, 515, 1293, 438] 
c_5 = [1512, 713, 1528, 732, 1538, 810] 
d_5 = [1421, 533, 1415, 473, 1364, 407] 

# --------------------------------------------------------------------- 
# Frame_6 

body_6 = [1656, 967, 1618, 908, 1521, 919, 1394, 998, 1410, 1031, 1579, 1016, 1645, 983] 
a_6 = [1525, 965, 1496, 1013, 1547, 1053] 
b_6 = [1403, 1010, 1470, 976, 1429, 1046] 
c_6 = [1604, 1004, 1605, 1017, 1588, 1046] 
d_6 = [1398, 1011, 1403, 1014, 1402, 1018] 

#============================================== 
#  Animation time control 
#============================================= 

def animdelay(cycle_period): 
    canvas_1.update()                    # This refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)   # This makes execution pause for cycle_period milliseconds. 
    canvas_1.delete('line_1')          # This erases everything on the canvas. 


#================================================ 
#  Interpolation Functions 
#================================================= 
def points_delta(number_of_steps, point_1, point_2): 
    """ 2D points, point_1 =  (x1,y1) and point_2 =  (x2,y2) are passed as arguments 
        and the straight line joining them is divided into N equally spaced differences, 
        where N = number_of_steps. 
    """ 
    x_delta = (point_2[0] - point_1[0])/float( number_of_steps) 
    y_delta = (point_2[1] - point_1[1])/float( number_of_steps) 
    return [x_delta, y_delta] 


def line_deltas(number_of_steps, line_1, line_2): 
    """ Lines, are passed as arguments in the form of 2D coordinate lists. 
        A list of the deltas for each sucessive pair of points is calculated. 
        The straight line joining each pair of corresponding points is 
        divided into equally spaced differences       
    """ 
    line_delta = [] 
    for i in range(0,len(line_1), 2): 
        xy_sub0 = [line_1[i], line_1[i+1]] 
        xy_sub1 = [line_2[i], line_2[i+1]] 
        xy_del = points_delta( number_of_steps, xy_sub0,  xy_sub1) 
        line_delta.append(xy_del) 
    # Flatten the resulting two dimensional list array. 
    flatten = itertools.chain.from_iterable(line_delta) 
    flat_line_delta = list(flatten) 
    return flat_line_delta 


def scale_shift_line(line, x_shift, y_shift, x_amp, y_amp): 
    """ Shift and amplify an entire line. 
    """ 
    xy_line = [] 
    for i in range(0, len(line), 2): 
         xx = line[i] * x_amp + x_shift 
         yy = line[i+1] * y_amp + y_shift 
         xy_line.append(xx) 
         xy_line.append(yy) 
    return  xy_line 

#================================================= 
# Animation set up constants: 
#================================================= 
# Convenient display position. 
x_shift, y_shift = 50, -100 
x_scale, y_scale = 0.6, 0.6 
stride = 1400                # The horizontal distance of a complete hop. 
scaled_stride = stride * x_scale 
cycle_period = 50   # Time between new positions of the ball (milliseconds). 
number_of_steps = 20         # Number of transition steps in the morph process. 

#====================================================== 
# Complete frames: 
#======================================================= 
frame_1 = [ body_1, a_1, b_1, c_1, d_1 ] 
frame_2 = [ body_2, a_2, b_2, c_2, d_2 ] 
frame_3 = [ body_3, a_3, b_3, c_3, d_3 ] 
frame_4 = [ body_4, a_4, b_4, c_4, d_4 ] 
frame_5 = [ body_5, a_5, b_5, c_5, d_5 ] 
frame_6 = [ body_6, a_6, b_6, c_6, d_6 ] 

#==================================================== 
# Frame Transition deltas: 
#================================================== 
""" The strategy behind these systematic frame-to-frame definitions here is to 
    pre-calaculate as much of the frame content as possible, prior to 
    animation rendering and thus avoid uncontrolled jerks and hesitations 
    in the smoothness of the animation. 
""" 
# 1  All body transitions 
body_1f2 = line_deltas(number_of_steps, frame_1[0], frame_2[0]) 
body_2f3 = line_deltas(number_of_steps, frame_2[0], frame_3[0]) 
body_3f4 = line_deltas(number_of_steps, frame_3[0], frame_4[0]) 
body_4f5 = line_deltas(number_of_steps, frame_4[0], frame_5[0]) 
body_5f6 = line_deltas(number_of_steps, frame_5[0], frame_6[0]) 

# 2  All foreleg_a transitions 
a_1f2 = line_deltas(number_of_steps, frame_1[1], frame_2[1]) 
a_2f3 = line_deltas(number_of_steps, frame_2[1], frame_3[1]) 
a_3f4 = line_deltas(number_of_steps, frame_3[1], frame_4[1]) 
a_4f5 = line_deltas(number_of_steps, frame_4[1], frame_5[1]) 
a_5f6 = line_deltas(number_of_steps, frame_5[1], frame_6[1]) 

# 3  All foreleg_b transitions 
b_1f2 = line_deltas(number_of_steps, frame_1[2], frame_2[2]) 
b_2f3 = line_deltas(number_of_steps, frame_2[2], frame_3[2]) 
b_3f4 = line_deltas(number_of_steps, frame_3[2], frame_4[2]) 
b_4f5 = line_deltas(number_of_steps, frame_4[2], frame_5[2]) 
b_5f6 = line_deltas(number_of_steps, frame_5[2], frame_6[2]) 

# 4  All hindleg_a transitions 
c_1f2 = line_deltas(number_of_steps, frame_1[3], frame_2[3]) 
c_2f3 = line_deltas(number_of_steps, frame_2[3], frame_3[3]) 
c_3f4 = line_deltas(number_of_steps, frame_3[3], frame_4[3]) 
c_4f5 = line_deltas(number_of_steps, frame_4[3], frame_5[3]) 
c_5f6 = line_deltas(number_of_steps, frame_5[3], frame_6[3]) 

# 5  All hindleg_b transitions 
d_1f2 = line_deltas(number_of_steps, frame_1[4], frame_2[4]) 
d_2f3 = line_deltas(number_of_steps, frame_2[4], frame_3[4]) 
d_3f4 = line_deltas(number_of_steps, frame_3[4], frame_4[4]) 
d_4f5 = line_deltas(number_of_steps, frame_4[4], frame_5[4]) 
d_5f6 = line_deltas(number_of_steps, frame_5[4], frame_6[4]) 

#=================================================== 
# Complete Transition delta frames: 
#================================================== 
delf_1to2 = [ body_1f2, a_1f2, b_1f2, c_1f2, d_1f2 ] 
delf_2to3 = [ body_2f3, a_2f3, b_2f3, c_2f3, d_2f3 ] 
delf_3to4 = [ body_3f4, a_3f4, b_3f4, c_3f4, d_3f4 ] 
delf_4to5 = [ body_4f5, a_4f5, b_4f5, c_4f5, d_4f5 ] 
delf_5to6 = [ body_5f6, a_5f6, b_5f6, c_5f6, d_5f6 ] 

#================================================== 
# Final assembly of principal frames and inter-frame transition deltas, ready for animation.  
#================================================== 

frame_sequence = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6 ] 
delta_frame_sequence = [ delf_1to2, delf_2to3, delf_3to4, delf_4to5, delf_5to6 ] 

#=========================================
#   Actual Animation.    
#===========================================

def run_frame_sequence(frame_sequence, delta_frame_sequence): 
    """ Run/animate a complete frame sequence from frame 1 to 13. 
    """ 
    for m in range(len(frame_sequence)-1): 
        for k in range(number_of_steps): 

            new_frame = [] 
            for j in range(len(frame_1)):  # Each part of the horse in a chosen frame 
                new_part = [] 
                for i in range(0, len(frame_sequence[m][j]), 2):       
                    newx_part_f1 = frame_sequence[m][j][i] +  k * delta_frame_sequence[m][j][i] 
                    newy_part_f1 = frame_sequence[m][j][i+1] +  k * delta_frame_sequence[m][j][i+1] 

                    new_part.append( newx_part_f1) 
                    new_part.append( newy_part_f1) 
                f2f_xy = scale_shift_line(new_part, x_shift, y_shift, x_scale, y_scale) 
                new_frame.append(f2f_xy) 
            for i in range(len(new_frame)): 

                canvas_1.create_line(new_frame[i], width=4, tag = 'line_1',  fill= 'blue')  
            animdelay(cycle_period)  

run_frame_sequence(frame_sequence, delta_frame_sequence) 

# First hop. 
x_shift += scaled_stride 
run_frame_sequence(frame_sequence, delta_frame_sequence) 

# Second hop. 
x_shift += scaled_stride 
run_frame_sequence(frame_sequence, delta_frame_sequence) 

# Third hop. 
x_shift += scaled_stride 
run_frame_sequence(frame_sequence, delta_frame_sequence) 

root.mainloop()
