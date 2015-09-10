"""
Program name: multi_shape_transmogrify_1.py
Objective: Transform a single point into a line of many points
(or a line of fewer points into a line of more points).

Keywords: Path, point, line expansion, shape,  animate.
============================================================================79
Comments:  The 'point_matcher(shape_1, shape_2) is the key to creative freedom
because the programmer only has to worry about shapes and not the error prone
 and tedious process of starting with different shapes that must have exactly
 the same number of points.

Tested on: Python versions 2.6, 2.7, 3.2
Author:          Mike Ohlson de Fine
"""
#from Tkinter import *
from tkinter import *  # For Python 3.2.3 and higher.

root = Tk()
root.title('Transmogrify three points into many.')
cw =350                                      # canvas width.
ch = 400                                     # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="black")
canvas_1.grid(row=0, column=1)
#==================================================================

# Morph Functions
def interpolation_delta(number_of_steps, num_1, num_2):
    """ Divide the numerical interval between two numbers, num_1 and num_2, 
        into an equal number of steps.
        The interval is divided into N equally spaced differences,
        where N = number_of_steps.
    """
    delta = (num_2 - num_1)/float( number_of_steps) 
    return delta

def line_deltas(number_of_steps, line_1, line_2):
    """ Lines, are passed as arguments in the form of 2D coordinate lists.
        A list of the deltas for each sucessive pair of points is calculated.
        The straight line joining each pair of corresponding points is divided
        into equally spaced differences       
    """
    line_delta = []
    for i in range(len(line_1)):
        new_value = interpolation_delta(number_of_steps, line_1[i], line_2[i])
        line_delta.append(new_value)
    return line_delta

def point_matcher(shape_1, shape_2):
    """  Make corresponding lines in each shape have the same number of points. 
       Strategy:
    *  Assume the shapes have the same number of lines, but different numbers of points.
    *  Compare the length (number of points) of each line in turn, 
    *  Compute the difference as 'dif'.
    *  Append repeat copies of the last point until the lengths are the same.
    """
    # Measure and compare the length of each line, one at a time.
    for k in range(len(shape_1)):                       # For each line.
         diff = (len(shape_1[k]) - len(shape_2[k]))/2       # Number of points difference for line k.
         # When a diference is discovered, add (append) duplicates of the last point to make up the difference.    

         last_x_shape_1 = shape_1[k][len(shape_1[k])-2] # Last x point component of line, shape_1. 
         last_y_shape_1 = shape_1[k][len(shape_1[k])-1] # Last y point component of line, shape_1. 

         last_x_shape_2 = shape_2[k][len(shape_2[k])-2] # Last x point component of line, shape_2. 
         last_y_shape_2 = shape_2[k][len(shape_2[k])-1] # Last y point component of line, shape_2. 

         if diff > 0:   # Append to shape_2 (shape_1 is longer than shape_2).
             for j in range(int(diff)): # Keep appending to shape_2 until lengths are the same.
                 shape_2[k].append(last_x_shape_2)
                 shape_2[k].append(last_y_shape_2)
         elif diff < 0:   # Append to shape_1 (shape_2 is longer than shape_1).
             for j in range(int(math.fabs(diff))): # Keep appending to shape_1 until lengths are the same.
                 shape_1[k].append(last_x_shape_1)  
                 shape_1[k].append(last_y_shape_1)                
    return shape_1, shape_2

# Test data and execution.
#==========================
# Each of three leaf shapes consists of 16 points.
three_leaves =  [[80, 59, 91, 50, 90, 34, 82, 24, 66, 17, 52, 14, 38, 16, 26, 17, 13, 16, 18, 28, 24, 40, 28, 54, 38, 65, 55, 72, 69, 71, 78, 61], [121, 87, 132, 89, 146, 86, 156, 78, 162, 63, 165, 49, 160, 33, 152, 23, 139, 9, 136, 24, 126, 33, 114, 43, 101, 56, 98, 70, 105, 82, 118, 85], [99, 101, 93, 91, 81, 84, 68, 83, 53, 89, 41, 97, 34, 111, 32, 125, 32, 144, 44, 135, 58, 135, 73, 136, 92, 136, 104, 129, 107, 115, 100, 104]]

# Each point below is the "seed" from which a 16-point leaf will grow.
three_points = [[20,20], [30,30], [40,40]]  

# Make each shape have the same number of points.
three_leaves, three_points = point_matcher(three_leaves, three_points) 

# Verify that the line-shapes in each set match in length.
#print ' three_leaves]: ', three_leaves
print ('len(three_leaves[0]): ' ,len(three_leaves[0]))
print ('len(three_leaves[1]): ' ,len(three_leaves[1]))
print ('len(three_leaves[2]): ' ,len(three_leaves[2]))

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('len(three_points[0]): ' ,len(three_points[0]))
print ('len(three_points[1]): ' ,len(three_points[1]))
print ('len(three_points[2]): ' ,len(three_points[2]))



# Draw the intermediate lines.
def morph_2D_shape(shape_start, shape_end, kula):
    """ Animate the gradual transition from one shape into another.
        Color in each polygon using a color array "kula".
    """
    xy_intermediate = []
    xy_intermediate_group = []
    xy_line_deltas = []
    xy_final = []
    delta_j = []
    xy0 = shape_start
    xy1 = shape_end
    for k in range(len(xy0)):
        del_j = line_deltas(number_of_steps, xy0[k], xy1[k])
        delta_j.append(del_j)

    for j in range(number_of_steps+1):
        for k in range(len(xy0)):
            for i in range(0, len(xy0[k]), 2):
                xx0 = (xy0[k][i]   + j * delta_j[k][i])   * x_scale + x_shift

                yy0 = (xy0[k][i+1] + j * delta_j[k][i+1]) * y_scale + y_shift 
                xy_intermediate.append(xx0)
                xy_intermediate.append(yy0)
            canvas_1.create_polygon(xy_intermediate, width=1, fill=kula[k])
            if k == len(xy0): xy_final = xy_intermediate
            xy_intermediate = []
        canvas_1.update()                    # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)         # This makes execution pause for 80 milliseconds.         
        canvas_1.delete(ALL)                 # This erases everything on the canvas 

# Final static images.
def display_2D_shape(shape_2D, kula):
    """ Display any multi-line shape as a color filled polygon.

          A matching color list (hex format = '#rrggbb') supplies the 
          color for each polygon belonging to the shape.
          A single color could be substituted by removing the [k]
          in the create_polygon() function.
    """
    xy_end   = []
    for k in range(len(shape_2D)):
        for i in range(0, len(shape_2D[k]), 2):
            xx1   = shape_2D[k][i]  * x_scale + x_shift
            yy1   = shape_2D[k][i+1]* y_scale + y_shift
            xy_end.append(xx1)
            xy_end.append(yy1)
        canvas_1.create_polygon(xy_end, width=5, fill= kula[k] )
        xy_end   = []

#=======================================================================
# Test and execution.
kula = ['#ff3100', '#a62000',  '#ff0700'] # Array of reddish volors for the leaves.
cycle_period = 80   # Time between new positions of the ball (milliseconds). 
number_of_steps = 100         # Number of transition steps in the morph process.

# Convenient display position.
x_shift, y_shift = 0, 20
x_scale, y_scale = 2., 2.

morph_2D_shape(three_points, three_leaves,kula)
display_2D_shape(three_leaves, kula)

root.mainloop()
