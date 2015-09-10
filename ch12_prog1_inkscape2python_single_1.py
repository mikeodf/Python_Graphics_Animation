""" 
Program name: inkscape2python_single_1.py
Objective: Transform an inkscape.svg drawing file into a single usable Python vertex list.
Specifically: Identify 2D vertices in all lines saved in a SVG file from an 
Inkscape drawing.
Each .svg line like:  d="M 82.833,90.697 L 97.985,78.575 L 118.19,99.788"
is converted to a Python list like:
[ 82.833,90.697 , 97.985,78.575 , 118.19,99.788  ]

Keywords: inkscape, conversion, drawing, vertices, lines,
============================================================================79 
Comments:
Input data used is an SVG file exported from Inkscape. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""

obj_file_name_1 = "/home/mikeodf/sun_moon_svgshapes/moonrise_4.svg"        # Inkscape output file.
#obj_file_name_1 = "/home/mikeodf/sun_moon_svgshapes/moon_ripples_3.svg" 
#obj_file_name_1 = "/home/mikeodf/sun_moon_svgshapes/just_sun_3.svg"   # Inkscape output file.


def extract_floats(line):
    """  Objective: Extract a complete floating point number, including sign.        
         Assumption: An appropriate line of characters ( the "line" argument)
         for parsing has been found. 
         Now we work through it character by character looking for minus signs, decimal points
         and digits. These are added to a string xx which will be converted to a float.
         A non-digit will signal the completion of the float.
    """
    slice_loc = 0                 # Slice position counter.
    line_length = len(line)       # Total length of line.
    sign = ''        # The sign (negative or positive) of the number.
    jadigit = 0      # Digit 'present' toggle flag.
    xx = ''          # xx will become the CURRENT floating point number.
    float_list = []

    # Pad the line with a space. Necessary to avoid loop index errors.
    line = line + ' '
    for chr in line:
    
        # Overriding condition. Only proceed if we are working inside the line length. 
        if slice_loc <= line_length-1:
        
            # Is character non-digit?
            if line[slice_loc].isdigit() == False:
         
                # Is character a minus sign?
                if line[slice_loc] == '-': 
                    sign = '-'
                    xx = sign
                slice_loc = slice_loc + 1       

            # Is character a digit?
            if  line[slice_loc].isdigit():
                jadigit = 1   
                xx = xx + line[slice_loc]     # Add the new digit to xx
                slice_loc = slice_loc + 1 

            # Is character a decimal point?
            if  line[slice_loc] == '.':
                jadigit = 1   
                xx = xx + line[slice_loc]       # Add this digit to xx
                slice_loc = slice_loc + 1 

            # The previous character was a digit but the current one is not 
            # Therefore the current floating point number is now complete.
            if  line[slice_loc].isdigit() == False and jadigit == 1:   # Terminate float.
                jadigit = 0   # Clear 'working up float' flag.
                sign = ''     # Clear the sign flag.
                float_list.append(float(xx))  # Add the latest float to the list
                slice_loc = slice_loc + 1 
                xx = ''

    return float_list    

id_start = ' d="M '   # Id signature for a valid vertex list in the inkscape.svg Data source.

def inkscape2python(svg_file):
    """  Open and parse an Inkscape SVG file and extract Python lists of (x,y) vertices.
         The returned 'line_set' is a two-dimensional list of complex shape vertices.
    """
    line_set = []
    file_lines = 0
    with open(svg_file) as ff:
        counter = 0          # Slice position counter.
        for line in ff:                # For each line ( line is the string contents of the line)
            line_length = len(line)     # Total length of line. Needed for number of slices.
            file_lines += 1             # Keep a count of the number of lines.
            if line.find(id_start) != -1:   # id_start string discovered. This denotes an SVG line of vertices.
                slice_loc = line.find(id_start) # The nxt character will be what we have been seeking -  a float.
                line_string = line
                floats_list = extract_floats(line)
                line_set.append(floats_list)
    return line_set

line_set_1 = inkscape2python(obj_file_name_1)
print 'moonscape = ', line_set_1

# ==========================
#  CONVERTED SHAPE  TESTING
# ==========================
from Tkinter import *
root = Tk()
root.title('Inkscape shapes converted to Python list.')
cw = 1600                                      # canvas width.
ch = 350                                      # canvas height.
canvas_1 = Canvas(root, width=cw, height=ch, background="#eeeeee")
canvas_1.grid(row=0, column=1)

for i in range(len(line_set_1)):
    canvas_1.create_line( line_set_1[i], width = 3,  fill= 'blue' )

root.mainloop()
