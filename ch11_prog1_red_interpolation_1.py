"""
Program name: red_interpolation_1.py
Objective: Creates sets of discrete transition sequences between two end colors.
The start and end colors are red channel values. Blue and Green are fixed at zero.

Keywords: canvas, color transition, sequence, color blending, discrete
============================================================================79
Comments: The start and end colors are given as as pairs of integer color values,
in the range 0 to 255. 
The user specifies how many transition steps there will be.
The colors are labelled with both their hexadecimal and rgb integer designations. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine.
"""
from Tkinter import *
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk()
root.title("Color transition from a start red to an end red")
canvas_1 = Canvas(root, width=800, height=870, background="black")
canvas_1.grid(row=0, column=1)

fnt = 'Bookantiqua 8 bold'
fnt_2 = 'Bookantiqua 8 bold'

def hex2rgb(hex_color):
    """ Convert a hex color of the from '#rrggbb'
        to three element tuple of base 10 integers corresponging to (red, green, blue).
    """
    start_kula = 0,0,0
    end_kula = 0,0,0
    n1 = [1,  3, 5]
    n2 = [3,  5, 7]
    rgb_color = []
    for i in range(0,3):
        a = n1[i]
        b = n2[i]
        kula_slice = hex_color[a:b]
        c = int(kula_slice, 16)
       
        rgb_color.append(c)  # '16' is the base from which to convert.
    rgb_color = tuple(rgb_color)
    return rgb_color

# Red inputs
def color_interpolation_series(start_red, end_red, num_steps):
    """ Create the color transion list between a start and an end color (red, green, blue).
         Generate Color Transition Series as hex RGB colors
    """
    delta_red = (end_red - start_red)/(num_steps - 1)
    color_series_hex = []
    for i in range(num_steps+1):
        next_red = start_red+i*delta_red
        if next_red <= 0.0:
            next_red = 0.0
        next_green = 0.0
        next_blue = 0.0
        next_color_int = next_red, next_green, next_blue
        next_color_hex = '#%02x%02x%02x' % next_color_int
        color_series_hex.append(next_color_hex)  
    return color_series_hex

def show_swatch(color_hex, x_start, y_start, width, height, gap):
    """  Paint a swatch specified by the xy position, width and height.
          'gap' is the vertical separation between swatches.
    """
    panel = x_start, y_start, x_start+width, y_start+height
    canvas_1.create_rectangle(panel, fill = color_hex)
    y_start = y_start + height + gap

    canvas_1.create_text(x_start + width+10, y_start-height, text= color_hex, fill='grey', width=200,
                         anchor=NW, font=fnt) #font='Bookantiqua 8 bold'
    color_int =  hex2rgb(color_hex)
    canvas_1.create_text(x_start + width+10, y_start-height+12, text= color_int, fill='grey', width=200,
                         anchor=NW, font=fnt_2) #font='Bookantiqua 8 bold'   
        
#==============================================
# Swatch geometry
#================
x_start = 20
y_start = 10
width = 150
height = 40
gap = 2
num_steps = 20

# Red Color transition tests
#==============================================
# Colors specified as integers
start_red_1 = 255
end_red_1   = 0

start_red_2 = 0
end_red_2   = 255

start_red_3 = 100
end_red_3   = 160

kulas = color_interpolation_series(start_red_1, end_red_1, num_steps )
for i in range(num_steps):
    show_swatch(kulas[i], x_start, y_start, width, height, gap)
    y_start += height+gap

x_start += width + 110
y_start = 10
kulas = color_interpolation_series(start_red_2, end_red_2, num_steps )
for i in range(num_steps):
    show_swatch(kulas[i], x_start, y_start, width, height, gap)
    y_start += height+gap

x_start += width + 110
y_start = 10
kulas = color_interpolation_series(start_red_3, end_red_3, num_steps )
for i in range(num_steps):
    show_swatch(kulas[i], x_start, y_start, width, height, gap)
    y_start += height+gap
#=========================================================

root.mainloop()
