"""
Program name: hopper_minimal_jump_1.py
Objective: Animate a seven stage Hopper jump. 

Keywords: Path, point, line, shape, intermediate positions, motion.
============================================================================79
Comments:  
Sub-divide the straight line path between two shapes, composed of
multiple lines, into a specified number of equi-spaced steps.
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
root.title('A Two-line hopper.')
cw = 1200                                      # canvas width.
ch = 600                                      # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0, column=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~   Digitized coordinates of line vertices for frog stick-figure.      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=====================================================================================================================
#------------------------------------------
# Frame 1
body_1 = [3, 1045, 91, 1025]
legs_1 = [52, 1034, -6, 1024, 52, 1053]
#-------------------------------------------
# Frame 2
body_2 = [24, 999, 98, 948]
legs_2 = [64, 972, 4, 971, 50, 1048]
#-------------------------------------------
# Frame 3
body_3 = [146, 811, 208, 746.]
legs_3 = [177., 778, 114, 811, 122, 889]
#-------------------------------------------
# Frame 4
body_4 = [316, 685, 406, 686]
legs_4 = [361, 685, 294, 662, 231, 639]
#-------------------------------------------
# Frame 5
body_5 = [505.7, 748.7, 578.3, 697.1]
legs_5 = [541, 722, 476, 722, 461, 784]
#-------------------------------------------
# Frame 6
body_6 = [630, 886, 601, 791]
legs_6 = [614, 839, 581, 890, 621, 950]
#-------------------------------------------
# Frame 7
body_7 = [640, 1043, 728, 1023]
legs_7 = [690, 1032, 632, 1022, 689, 1051]
#-------------------------------------------

def animdelay(cycle_period):
    """ Animation function (draw-delay-erase).
        The input argument cycle_period is the time delay in milliseconds.
    """
    canvas_1.update()              # This refreshes the drawing on the canvas.
    canvas_1.after(cycle_period)   # This makes execution pause for 100 milliseconds.
    canvas_1.delete('line_1')      # This erases everything on the canvas.


# Morph Functions
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
        The straight line joining each pair of corresponding points is divided into equally spaced differences       
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
    """ Shift and amplify an entire line
    """
    xy_line = []
    for i in range(0, len(line), 2):
         xx = line[i] * x_amp + x_shift
         yy = line[i+1] * y_amp + y_shift
         xy_line.append(xx)
         xy_line.append(yy)
    return  xy_line

#========================================================================
# Animation set up constants:
#========================================================================
# Convenient display position.
x_shift, y_shift = 50, -550
x_scale, y_scale = 0.8, 1.0
stride = 633                 # The horizontal distance of a complete hop.
scaled_stride =stride * x_scale
cycle_period = 30            # Time between new positions of the ball (milliseconds).
number_of_steps = 10         # Number of transition steps in the morph process.

#========================================================================
# Complete frames:
#========================================================================
frame_1 = [ body_1, legs_1 ]
frame_2 = [ body_2, legs_2 ]
frame_3 = [ body_3, legs_3 ]
frame_4 = [ body_4, legs_4 ]
frame_5 = [ body_5, legs_5 ]
frame_6 = [ body_6, legs_6 ]
frame_7 = [ body_7, legs_7 ]

#========================================================================
# Frame Transition deltas:
#========================================================================
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
body_6f7 = line_deltas(number_of_steps, frame_6[0], frame_7[0]) 

# 2  All leg_a transitions
a_1f2 = line_deltas(number_of_steps, frame_1[1], frame_2[1])
a_2f3 = line_deltas(number_of_steps, frame_2[1], frame_3[1]) 
a_3f4 = line_deltas(number_of_steps, frame_3[1], frame_4[1])
a_4f5 = line_deltas(number_of_steps, frame_4[1], frame_5[1])
a_5f6 = line_deltas(number_of_steps, frame_5[1], frame_6[1]) 
a_6f7 = line_deltas(number_of_steps, frame_6[1], frame_7[1])

#========================================================================
# Complete Transition delta frames:
#========================================================================
delf_1to2 = [ body_1f2, a_1f2 ]
delf_2to3 = [ body_2f3, a_2f3 ]
delf_3to4 = [ body_3f4, a_3f4 ]
delf_4to5 = [ body_4f5, a_4f5 ]
delf_5to6 = [ body_5f6, a_5f6 ]
delf_6to7 = [ body_6f7, a_6f7 ]

#==================================================================================================
""" Final assembly of principal frames and inter-frame transition deltas, ready for animation.  """
#===================================================================================================
frame_sequence = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7 ]
delta_frame_sequence = [ delf_1to2, delf_2to3, delf_3to4, delf_4to5, delf_5to6, delf_6to7 ]

#==================================================================================================
""" Actual Animation.    """
#==================================================================================================

def run_frame_sequence(frame_sequence, delta_frame_sequence):
    """ Run/animate a complete frame sequence from frame 1 to 7.
    """
    for m in range(len(frame_sequence)-1):
        for k in range(number_of_steps):

            new_frame = []
            for j in range(len(frame_1)):  # Each part of the object in a chosen frame
                new_part = []
                for i in range(0, len(frame_sequence[m][j]), 2):   
                    newx_part_f1 = frame_sequence[m][j][i] +  k * delta_frame_sequence[m][j][i]
                    newy_part_f1 = frame_sequence[m][j][i+1] +  k * delta_frame_sequence[m][j][i+1]

                    new_part.append( newx_part_f1)
                    new_part.append( newy_part_f1)
                f2f_xy = scale_shift_line(new_part, x_shift, y_shift, x_scale, y_scale)
                new_frame.append(f2f_xy)
            for i in range(len(new_frame)):
                canvas_1.create_line(new_frame[i], width=2, tag = 'line_1',  fill= 'blue')  
            animdelay(cycle_period)  

# First hop
run_frame_sequence(frame_sequence, delta_frame_sequence)

# Second hop
x_shift += scaled_stride
run_frame_sequence(frame_sequence, delta_frame_sequence)

# Third hop
x_shift += scaled_stride
run_frame_sequence(frame_sequence, delta_frame_sequence)

# Fourth hop
x_shift += scaled_stride
run_frame_sequence(frame_sequence, delta_frame_sequence)

root.mainloop()

