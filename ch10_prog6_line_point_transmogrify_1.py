"""
Program name: line_point_transmogrify_1.py
Objective: Transform a single point into an object of many points and lines.

Keywords: Path, point, line expansion, shape expansion, object matching,  animate.
============================================================================79
Comments:  The 'point_matcher' and 'line_mathaer' are the key to creative freedom
because the programmer only has to worry about initial and final shapes.
By starting with a single virtual point the transmogrification degenerates into
a simpe scale and translation.

Tested on: Python versions 2.6, 2.7, 3.2
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
import random

root = Tk()
root.title('Transmogrify thirty-eight lines from nothing.')
cw =1000                                      # canvas width.
ch = 600                                      # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background='#080136')
canvas_1.grid(row=0, column=1)

# Test data.
#==========================
# Two_roses - 38 lines
two_roses = [[121, 894, 120, 905, 122, 920, 128, 939, 136, 957, 145, 978, 148, 993, 148, 1008, 147, 1022, 145, 1035, 150, 1037, 153, 1021, 153, 1008, 153, 995, 149, 978, 142, 960, 135, 947, 129, 934, 125, 920, 123, 905, 125, 895], [115, 887, 116, 879, 121, 875, 125, 878, 131, 881, 136, 882, 138, 887, 134, 893, 134, 890, 134, 887, 131, 885, 129, 889, 125, 892, 120, 891, 120, 885, 122, 881, 118, 881, 117, 883], [128, 874, 126, 874, 122, 868, 110, 860, 109, 846, 110, 846, 114, 852, 123, 862, 128, 872], [131, 872, 127, 862, 112, 844, 111, 831, 118, 816, 122, 810, 123, 811, 119, 821, 121, 834, 129, 851, 132, 866, 132, 870], [136, 862, 134, 851, 124, 834, 125, 820, 132, 806, 133, 806, 131, 814, 134, 827, 144, 844, 143, 854, 138, 861], [135, 817, 134, 810, 137, 802, 144, 796, 145, 793, 146, 793, 145, 799, 137, 809, 136, 816], [144, 855, 146, 851, 146, 841, 138, 826, 138, 819, 140, 817, 142, 820, 148, 833, 160, 843, 169, 847, 175, 847, 177, 850, 171, 851, 157, 851, 149, 853, 145, 856], [153, 832, 151, 828, 145, 823, 145, 815, 149, 809, 154, 807, 152, 811, 155, 820, 155, 829, 154, 832], [142, 817, 141, 811, 143, 803, 150, 800, 158, 801, 153, 804, 146, 809, 144, 813], [158, 826, 156, 819, 156, 812, 159, 810, 161, 814, 160, 819, 160, 824, 159, 826], [162, 821, 163, 817, 163, 813, 166, 814, 169, 817, 170, 820, 166, 820, 164, 821], [158, 806, 163, 804, 168, 805, 171, 810, 176, 815, 180, 818, 181, 823, 180, 829, 178, 829, 177, 823, 175, 819, 171, 817, 167, 812, 165, 808, 159, 807], [131, 878, 138, 874, 148, 875, 157, 880, 162, 882, 158, 884, 152, 884, 147, 880, 138, 878, 132, 879], [139, 871, 147, 870, 161, 871, 171, 872, 178, 869, 181, 866, 180, 870, 175, 877, 169, 880, 161, 878, 153, 874, 148, 872, 141, 872], [136, 866, 143, 859, 152, 855, 166, 855, 180, 854, 186, 852, 188, 849, 186, 854, 183, 860, 177, 866, 170, 868, 161, 868, 151, 866, 143, 866, 137, 867], [154, 834, 159, 831, 170, 832, 174, 831, 176, 829, 175, 834, 173, 839, 171, 843, 166, 844, 160, 840, 157, 836, 154, 834], [179, 851, 181, 848, 179, 845, 176, 843, 177, 838, 181, 835, 186, 839, 186, 846, 184, 850, 180, 851], [188, 847, 193, 843, 193, 836, 191, 831, 192, 826, 189, 830, 187, 836, 189, 842, 189, 846], [158, 829, 166, 829, 171, 829, 174, 824, 169, 823, 164, 824, 160, 827, 159, 828], [88, 910, 88, 912, 84, 919, 82, 936, 73, 941, 70, 941, 74, 933, 80, 918, 86, 911], [82, 907, 76, 916, 66, 943, 56, 949, 42, 945, 37, 940, 37, 938, 46, 941, 56, 933, 67, 917, 77, 908, 81, 907], [73, 906, 65, 912, 54, 928, 42, 932, 29, 929, 29, 928, 36, 927, 45, 919, 56, 903, 64, 900, 72, 904], [35, 913, 32, 920, 24, 924, 16, 921, 14, 923, 13, 918, 18, 913, 29, 917, 34, 913], [68, 898, 64, 896, 55, 899, 44, 912, 40, 916, 39, 909, 44, 903, 49, 897, 56, 883, 58, 871, 55, 864, 58, 861, 60, 866, 62, 884, 65, 892, 68, 896], [47, 893, 44, 895, 40, 903, 34, 905, 28, 902, 26, 897, 30, 898, 37, 893, 44, 891, 46, 891], [36, 908, 31, 911, 24, 910, 21, 903, 20, 893, 23, 898, 28, 905, 32, 908], [41, 888, 35, 891, 29, 893, 27, 890, 30, 887, 35, 886, 39, 886, 40, 886], [36, 884, 32, 884, 29, 884, 29, 880, 32, 875, 33, 875, 35, 879, 36, 881, 36, 881], [22, 891, 19, 885, 20, 879, 24, 874, 27, 868, 29, 862, 32, 860, 41, 858, 39, 862, 33, 865, 31, 868, 29, 873, 26, 878, 23, 882, 23, 889], [88, 908, 85, 901, 89, 886, 96, 881, 97, 871, 101, 881, 100, 886, 93, 892, 89, 901, 89, 907], [81, 900, 80, 891, 82, 874, 83, 862, 80, 855, 76, 850, 80, 852, 89, 858, 92, 866, 90, 874, 85, 884, 82, 889, 82, 898], [76, 903, 71, 897, 67, 887, 65, 870, 63, 853, 61, 847, 59, 844, 63, 846, 68, 849, 73, 856, 76, 864, 77, 874, 76, 886, 76, 895, 78, 903], [48, 891, 45, 885, 44, 872, 43, 868, 41, 866, 45, 866, 49, 867, 53, 869, 54, 875, 52, 883, 49, 887, 48, 890], [59, 858, 56, 856, 53, 860, 52, 863, 48, 863, 45, 858, 47, 853, 53, 850, 57, 852, 59, 856], [54, 847, 48, 844, 40, 846, 37, 851, 32, 852, 37, 855, 43, 855, 47, 849, 52, 847], [42, 880, 41, 873, 40, 870, 37, 868, 35, 871, 35, 874, 37, 876, 40, 879], [102, 920, 94, 921, 89, 917, 91, 912, 93, 906, 93, 901, 98, 898, 104, 900, 102, 901, 99, 902, 98, 905, 102, 907, 105, 910, 105, 914, 100, 916, 95, 915, 96, 918, 99, 919], [107, 911, 118, 918, 131, 929, 145, 947, 156, 965, 162, 979, 167, 995, 169, 1007, 170, 1019, 171, 1029, 171, 1036, 164, 1035, 165, 1027, 165, 1013, 163, 997, 160, 987, 156, 973, 148, 958, 140, 946, 129, 932, 116, 921, 106, 915]]

# Color  array
stem_green = '#105017'
red_dark_1 = '#970b12'
red_dark_2 = '#4b070a'
red_light_1 = '#cd1622'
red_light_2 = '#dd0915'

kula = [ stem_green, stem_green, red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2, red_light_1, red_light_2,  red_light_1, red_light_2, red_light_1, red_light_2, red_light_1, red_light_2, red_light_1,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2,  red_dark_1, red_dark_2, red_light_2, stem_green, stem_green ]

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

def line_matcher(shape_1, shape_2):
    """  Force two objects to have the same number of lines. 
         Both objects must end up with the same number of lines as the larger of the two.
         However each new line will in fact only consist of  single point.
       Strategy:
    *  Compare the size (number of lines) of each shape in turn, 
    *  Compute the difference as 'dif'.
    *  Append single-point lines anywhere inside the canvas until the sizes are the same.
    """
    dif = (len(shape_1) - len(shape_2))
    if dif > 0 :  # Shape_1 has more lines than shape_2      
        for i in range(dif):
            shape_2.append([random.randint(0,cw), random.randint(0,ch)])   # Add a single point "line". 
    if dif < 0 :  # Shape_2 has more lines than shape_1
        dif = -dif
        for i in range(dif):
            shape_1.append([random.randint(0,cw), random.randint(0,ch)]) 
    
    return shape_1, shape_2   

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
                ''' Scaling and shifting for convenient viewing.
                '''
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

#=================================================================
# Test and execution

# The point below is the "seed" from which all 38 shapes for the roses will grow..
#virtual_points_1 = [[20,20]]
virtual_points_1 = [[cw,200]]

# Make each ojject (a group of line-shapes) have the same number of shapess.
two_roses, virtual_points_1 = line_matcher(two_roses, virtual_points_1) 
# Make each shape have the same number of points.
two_roses, virtual_points_1 = point_matcher(two_roses, virtual_points_1) 

cycle_period = 120   # Time between new positions of the ball (milliseconds). 
number_of_steps = 200         # Number of transition steps in the morph process.
# Convenient display position.
x_shift, y_shift = 100, -1200
x_scale, y_scale = 1.8, 1.8

morph_2D_shape(virtual_points_1, two_roses,kula)
display_2D_shape(two_roses, kula)

root.mainloop()
