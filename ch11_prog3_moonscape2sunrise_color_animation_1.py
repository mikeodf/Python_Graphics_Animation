"""
Program name: moonscape2sunrise_color_animation_1.py
Objective: Demonstrate color interpolation applied to a landscape image.

Keywords: color transition, sequence, color blending, landscape image
============================================================================79
Comments: The start and end colors are given Python lists that are matched to 
polygon areas composing a landscape image.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine 
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk()
root.title("Landscape with color interpolation.")
canvas_1 = Canvas(root, width=1400, height=850, background="black")
canvas_1.grid(row=0, column=1)

#=============================================================================
# The various polygon shapes making up the picture.
msc_0 = [0, -16, 217, -16, 218, 104, 0, 104]  # area 0.
msc_1 = [0, 37, 31, 18, 62, 6, 111, 0, 88, 9, 51, 32, 46, 34, 39, 33, 30, 39, 0, 50]  # area 1.
msc_2 = [111, 0, 86, 8, 49, 31, 97, 14, 123, 9, 153, 7, 191, 10, 218, 15, 218, 0]  # area 2.
msc_3 = [55, 28, 96, 13, 123, 8, 153, 6, 190, 8, 218, 15, 217, 28, 188, 25, 155, 25, 108, 29, 50, 38, 44, 33]  # area 3.
msc_4 = [50, 38, 107, 27, 155, 24, 189, 25, 218, 28, 218, 41, 191, 39, 191, 39, 103, 44, 104, 44, 77, 51, 62, 46, 55, 41]  # area 4.
msc_5 = [103, 44, 192, 39, 218, 40, 217, 52, 204, 53, 194, 48, 166, 50, 153, 56, 144, 51, 133, 56, 122, 56, 123, 56, 105, 62, 105, 62, 76, 50]  # area 5.
msc_6 = [153, 55, 167, 49, 167, 49, 194, 48, 194, 48, 203, 51, 217, 52, 217, 52, 218, 60, 217, 60, 181, 55]  # area 6.
msc_7 = [95, 67, 122, 55, 133, 56, 144, 50, 153, 54, 182, 55, 182, 55, 218, 60, 218, 60, 218, 67]  # area 7.
msc_8 = [29, 39, 38, 33, 40, 33, 44, 33, 54, 40, 62, 46, 80, 52, 106, 62, 96, 67, 0, 67, 0, 50]  # area 8.
msc_9 = [29, 40, 30, 43, 34, 41, 35, 41, 39, 43, 44, 46, 49, 47, 47, 45, 46, 43, 51, 45, 55, 47, 57, 46, 53, 42, 59, 45, 53, 40, 46, 35, 44, 33, 39, 33, 33, 37, 30, 39, 30, 39]  # area 9.
msc_10 = [0, 66, 71, 66, 251, 67, 218, 67, 217, 70, 0, 70]  # area 10.
msc_11 = [0, 70, 217, 70, 217, 76, 0, 76]  # area 11.
msc_12 = [0, 76, 217, 75, 218, 86, 113, 86, 92, 84, 0, 84]  # area 12.
msc_13 = [0, 84, 218, 84, 218, 95, 114, 94, 92, 95, 0, 95]  # area 13.  
msc_14 = [0, 95, 0, 95, 217, 94, 217, 94, 218, 108, 0, 108]  # area 14.

#=============================================================================

def hex2rgb(hex_color):
    """ Take a hex color in the form '#rrggbb' and separate the color channels out 
        into the equivalent decimal integers (range from 0 to 255).
    """
    rhex = hex_color[1:3] 
    ghex = hex_color[3:5] 
    bhex = hex_color[5:7] 
    rdec = int(rhex,16)
    gdec = int(ghex,16)
    bdec = int(bhex,16)     
    return rdec, gdec, bdec

# Hex color inputs.
def discrete_kula_series(start_color, end_color, num_steps):
    """ Create the color transion list between a start and an end color (hex rgb).
         Generate Color Transition Series as hex RGB inputs
    """
    start_color_int = hex2rgb(start_color)
    end_color_int = hex2rgb( end_color)

    delta_red = (end_color_int[0] - start_color_int[0])/(num_steps - 1)
    delta_green = (end_color_int[1] - start_color_int[1])/(num_steps - 1)
    delta_blue = (end_color_int[2] - start_color_int[2])/(num_steps - 1)
    color_series_int = []
    color_series_hex = []
    for i in range(num_steps):
    #for i in range(num_steps+1):
    #for i in range(num_steps+5):
        next_red = start_color_int[0]+i*delta_red
        if next_red <=0.0:
            next_red = 0.0
        if next_red >= 255.0:
            next_red = 255
        next_green = start_color_int[1]+i*delta_green
        if next_green <=0.0:
            next_green = 0.0
        if next_green >= 255.0:
            next_green = 255
        next_blue = start_color_int[2]+i*delta_blue
        if next_blue <=0.0:
            next_blue = 0.0
        if next_blue >= 255.0:
            next_blue = 255
        next_color_int = next_red, next_green, next_blue
        color_series_int.append(next_color_int)
        if i < num_steps:
            next_color_hex = '#%02x%02x%02x' % next_color_int
            color_series_hex.append(next_color_hex)
            color_series_int.append(next_color_int)
        else:
            next_color_hex =  '#%02x%02x%02x' % end_color_int
            color_series_hex.append(next_color_hex)  
            color_series_int.append(next_color_int)
        
    return color_series_hex

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
#  Animation time control
#========================================================================
def animdelay(cycle_period):
    canvas_1.update()              # This refreshes the drawing on the canvas.
    canvas_1.after(cycle_period)   # This makes execution pause for 100 milliseconds.
    canvas_1.delete('line_1')      # This erases everything on the canvas.


# Sun and Moon rise color series.
#================================

# Moonlight
kmr_0 = '#101859'  # area 1 -background
kmr_1 = '#1c1886'  # area 2 
kmr_2 = '#461886'  # area 3
kmr_3 = '#5c1891'  # area 4
kmr_4 = '#6414e6'  # area 5
kmr_5 = '#6636f6'  # area 6
kmr_6 = '#3e4976'  # area 7
kmr_7 = '#1b243b'  # area 8
kmr_8 = '#793489'  # area 9
kmr_9 = '#b950c9'  # area 10
kmr_10 = '#33146b' # area 11
kmr_11 = '#9461c9' # area 15
kmr_12 = '#51146b' # area 12
kmr_13 = '#741ba9' # area 13
kmr_14 = '#8b46bb' # area 14

# Predawn
ksr_0 = '#391150'  # area 0
ksr_1 = '#511169'  # area 1
ksr_2 = '#631150'  # area 2
ksr_3 = '#71085b'  # area 3
ksr_4 = '#a40840'  # area 4
ksr_5 = '#c91431'  # area 5
ksr_6 = '#63143c'  # area 6
ksr_7 = '#310113'  # area 7
ksr_8 = '#510126'  # area 8
ksr_9 = '#f67bbc'   # area 9
ksr_10 = '#410134' # area 10
ksr_11 = '#64014b' # area 11
ksr_12 = '#990140' # area 12
ksr_13 = '#a40b26' # area 13
ksr_14 = '#e62613' # area 14

# Sunrise 
kss_0 = '#7686f9'  # area 0
kss_1 = '#c6a0f9'  # area 1
kss_2 = '#f8e376'  # area 2
kss_3 = '#feb004'  # area 3
kss_4 = '#f69b0c'  # area 4
kss_5 = '#f8400c'  # area 5
kss_6 = '#86569c'  # area 6
kss_7 = '#9e74c0'  # area 7
kss_8 = '#a671b1'  # area 8
kss_9 = '#fec38b'  # area 9
kss_10 = '#9e2040' # area 10
kss_11 = '#ff2e16' # area 11
kss_12 = '#f9492c' # area 12
kss_13 = '#f95b2e' # area 13
kss_14 = '#ffb12b' # area 14

# The color lists for each separate picture (kulas arrays).
sunshine_palette  =  [  kss_0, kss_1, kss_2, kss_3, kss_4, kss_5, kss_6, kss_7, kss_8, kss_9, kss_10, kss_11, kss_12, kss_13, kss_14 ]
moonlight_palette =  [  kmr_0, kmr_1, kmr_2, kmr_3, kmr_4, kmr_5, kmr_6, kmr_7, kmr_8, kmr_9, kmr_10, kmr_11, kmr_12, kmr_13, kmr_14 ] 
dawn_palette      =  [  ksr_0, ksr_1, ksr_2, ksr_3, ksr_4, ksr_5, ksr_6, ksr_7, ksr_8, ksr_9, ksr_10, ksr_11, ksr_12, ksr_13, ksr_14 ]

# The shapes making up the picture.
moonscape = [ msc_0, msc_1,  msc_2,  msc_3,  msc_4,  msc_5,  msc_6,  msc_7,  msc_8,  msc_9,  msc_10,  msc_11,  msc_12,  msc_13,  msc_14]

#==============================================

# Test the animation.
x_shift = 50
y_shift = 150
x_amp = 6
y_amp = 6
num_steps = 150

# Create the 3D color array:
#===========================
"""
Across horizontally (controlled by the j index) we have a polygon
for each area on the moonscape vector image.
In the time-axis direction (z or depth) we have the i axis for color transitions.
These should be contained sequentialy in the kulas[j][i] arrays.
"""
# Create the arrays of intermediate transition colors.
moon2dawn = []
dawn2sun = []
for j in range(len(moonlight_palette)):
    moon2dawn_j = discrete_kula_series(moonlight_palette[j], dawn_palette[j], num_steps )
    moon2dawn.append(moon2dawn_j)
    dawn2sun_j = discrete_kula_series(dawn_palette[j],sunshine_palette[j], num_steps )
    dawn2sun.append(dawn2sun_j)

# Scale and shift to convenient viewing position.
for i in range(len(moonlight_palette)): 
    moonscape[i] = scale_shift_line(moonscape[i], x_shift, y_shift, x_amp, y_amp)  
'''
# Verify correct color assignment for moonlight.
for j in range(len(moonlight_palette)): 
    canvas_1.create_polygon(moonscape[j], fill = moonlight_palette[j])

# Verify correct color assignment for pre-dawn.
for j in range(len(moonlight_palette)): 
    canvas_1.create_polygon(moonscape[j], fill = dawn_palette[j])

# Verify correct color assignment for sunrise.
for j in range(len(moonlight_palette)): 
    canvas_1.create_polygon(moonscape[j], fill = dawn_palette[j])
'''

for j in range(len(moonlight_palette)): 
    canvas_1.create_polygon(moonscape[j], fill = moonlight_palette[j])
cycle_period = 2000  # Hold the start image for 2 seconds.
animdelay(cycle_period)
cycle_period = 50   # Commence animation at an update frame period of 50 milliseconds.
for i in range(num_steps): 
    for j in range(len(moonlight_palette)): 
        canvas_1.create_polygon(moonscape[j], fill = moon2dawn[j][i])
    animdelay(cycle_period)
cycle_period = 2000  # Hold the pre-dawn image for 2 seconds.
animdelay(cycle_period)
cycle_period = 50 # Commence animation at an update frame period of 50 milliseconds.
for i in range(num_steps): 
    for j in range(len(moonlight_palette)): 
        canvas_1.create_polygon(moonscape[j], fill = dawn2sun[j][i])
    animdelay(cycle_period)

for j in range(len(moonlight_palette)): # Destination static image.
    canvas_1.create_polygon(moonscape[j], fill = sunshine_palette[j])

#================================================================================
root.mainloop()
