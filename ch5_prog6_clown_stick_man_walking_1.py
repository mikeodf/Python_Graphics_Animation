"""
Program name: clown_stick_man_walking_1.py
Objective: Demontrate code for a clown stick man walking with detailed head,
 hands and shoes.

Keywords: canvas, clown stick man, walking
============================================================================79 
Comments: Substitute Inkscape drawn head, hands and feet for appendages of a stick man.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import time
root = Tk()
root.title("Clown Walking.") 

cw = 1600                                   # canvas width
ch = 550                                    # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 100 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 100 milliseconds.
    chart_1.delete('line_1')      # This erases everything on the canvas.

#=======================================================================
# Stick-man joint time-trajectories.  
head =[ 25.91,32.46 , 30.78,34.73 , 43.13,30.98 , 50.85,32.85 , 59.24,32.08 , 64.2,34.73 , 77.44,30.65 , 84.83,32.96 , 93.77,32.41 ]
shoulder = [ 23.94,42.34 , 27.8,42.45 , 40.82,39.91 , 49.53,42.23 , 57.14,42.56 , 61.67,42.34 , 75.34,39.47 , 83.18,41.9 , 91.89,42.45]
hips = [ 23.09,64.24 , 25.04,65.88 , 38.3, 61.12 , 46.72,62.21 , 56.63,63.93 , 58.97,65.95 , 72.78,60.88 , 80.66,61.82 , 91.34,63.93]
#  ...............................................................................
knee_a = [ 30.42,79.29 , 39.16,77.11 , 38.22,75.24 , 44.93,75.47 , 46.72,77.66 , 51.87,79.92 , 81.12,74.22 , 91.34,72.66 , 98.21,78.2]
heel_b = [ 2.152,90.73 , 5.134,88.92 , 29.22,80.15 , 45.65,83.55 , 68.64,96.19 , 68.82,95.86 , 69.36,93.91 , 69.65,92.82 , 70.2,90.6]

knee_b = [ 13.1,78.44  , 18.33,79.84 , 46.49,74.3  , 57.18,72.74 , 63.57,78.44 , 72.23,77.11 , 73.01,74.38 , 79.33,75.16 , 81.28,78.12]
heel_a = [ 35.02,96.28 , 35.3,95.9 , 35.3,94.13 , 35.52,92.42 , 35.74,90.38 , 38.61,89 , 63.82,79.79 , 79.43,83.43 , 103.1,96.06]
#  ...............................................................................
elbow_a = [ 14.06,46.31 , 15.28,50.56 , 35.25,51.17 , 54.83,53.81 , 65.14,51.66 , 72.53,52.99 , 76.17,52.32 , 76.78,52.43 , 83.01,50.39 ]
wrist_a = [ 9.046,65.01 , 2.703,57.62 , 38.06,68.15 , 62.99,61.7 , 72.64,62.8 , 86.43,60.05 , 82.51,66.11 , 74.57,63.8 , 77,64.84 ]

elbow_b = [ 30.17,50.72 , 38.78,52.71 , 41.75,52.66 , 42.47,52.77 , 48.59,50.34 , 47.71,46.48 , 69.77,50.78 , 88.64,53.92 , 98.79,51.17 ]
wrist_b = [ 39.33,63.58 , 52.78,60.1 , 47.99,66 , 40.6,64.18 , 42.64,64.46 , 36.24,57.9 , 72.59,67.71 , 96.85,61.87 , 107.1,62.78 ]
#======================================================================================================================
# Drawn outlines.
shoe = [ 30.78,14.58 , 30.24,17.79 , 29.17,21.03 , 27.81,23.73 , 25.76,26.55 , 24.2,31.05 , 23.96,38.25 , 26.25,39.99 , 30.14,41.07 , 38.37,40.23 , 46.37,40.17 , 56.5,40.17 , 65.36,40.11 , 71.1,38.79 , 74.4,34.59 , 76.2,29.19 , 76.02,24.75 , 74.88,20.97 , 72.6,18.21 , 69.67,16.03 , 65.75,14.89 , 62.58,15.9 , 59.61,17.79 , 57.27,20.73 , 55.96,23.07 , 52.5,24.03 , 49.19,22.89 , 45.09,22.77 , 43.1,20.43 , 42.27,17.79 , 41.64,15.67 , 40.91,13.48 , 38.23,14.52 , 34.33,14.64 , 32.09,14.74 , 32.09,14.74 ]

hand = [ 52.38,12.31 , 53.38,14.65 , 52.28,17.68 , 49.08,20.23 , 46.18,21.63 , 42.28,22.93 , 39.68,23.13 , 38.28,24.83 , 40.08,26.73 , 43.98,29.23 , 51.08,31.23 , 62.48,34.83 , 63.58,35.73 , 63.88,37.13 , 63.08,38.93 , 61.98,39.93 , 59.08,39.53 , 54.08,38.43 , 49.18,37.33 , 44.78,36.63 , 42.48,36.63 , 41.08,37.13 , 42.28,38.83 , 45.98,42.13 , 50.28,46.03 , 54.58,49.33 , 57.78,52.03 , 58.88,53.43 , 58.88,55.63 , 57.28,57.13 , 55.18,56.73 , 52.58,55.13 , 48.68,51.83 , 44.18,48.13 , 40.28,45.13 , 37.68,43.33 , 36.18,43.43 , 36.28,44.63 , 37.38,48.33 , 39.98,52.63 , 42.48,56.93 , 44.48,60.83 , 45.18,63.23 , 44.78,64.93 , 43.18,65.93 , 41.18,65.53 , 39.68,63.63 , 37.68,59.83 , 35.68,55.73 , 33.58,52.13 , 31.38,48.83 , 29.18,46.53 , 28.21,46.23 , 27.25,47.53 , 27.24,51.63 , 27.59,56.03 , 27.94,59.83 , 27.77,61.83 , 27.05,63.03 , 26,63.43 , 24.88,63.03 , 23.77,62.33 , 23.05,60.33 , 22.58,56.63 , 22.06,52.63 , 21.56,49.63 , 21.07,46.93 , 20.81,44.93 , 18.59,42.93 , 17.36,40.63 , 15.48,37.53 , 13.6,34.23 , 12.39,30.33 , 12.8,27.73 , 14.48,25.13 , 16.75,23.53 , 18.61,22.33 , 19.48,19.73 , 21.26,16.84 , 24.62,14.95 , 29.28,14.48 , 32.58,15.27 , 37.18,16.06 , 42.08,15.96 , 46.48,14.69 , 49.78,13.72 , 51.98,12.38 ]

clown_head = [ 105.7,50.47 , 109,39.54 , 117,31.52 , 130.6,28.61 , 144.3,32.43 , 154.5,38.81 , 159.8,47.74 , 162,54.98 , 156.9,55.26 , 154.7,48.47 , 151.8,44.28 , 149.8,46.46 , 152.5,50.29 , 153.8,54.84 , 149,57.21 , 150,60.67 , 154.7,59.22 , 155.2,63.77 , 156,70.69 , 158.3,70.51 , 158.7,65.59 , 157.2,59.03 , 162.2,57.58 , 162,62.5 , 164.7,65.41 , 169.5,63.22 , 175.1,59.94 , 182.6,59.58 , 188.2,64.14 , 191.5,72.33 , 191,79.99 , 184.9,86.73 , 176.4,88.37 , 167.8,86.36 , 160.2,82.9 , 154.9,78.89 , 149.8,75.07 , 144.1,71.24 , 137.6,71.24 , 133.4,74.89 , 131.4,83.27 , 133.2,93.11 , 139.8,103.7 , 148,109.3 , 156.9,111 , 164.7,109.7 , 169.5,108.4 , 171.6,102.8 , 170.5,98.21 , 162,97.48 , 151.8,93.65 , 146.1,90.19 , 142.5,86.55 , 140.5,83.08 , 139,83.81 , 136.7,86.55 , 135.4,85.64 , 135.4,82.9 , 138.5,79.62 , 143.6,78.53 , 148,79.08 , 150.5,80.9 , 149.8,83.27 , 146.3,82.9 , 145.6,84.36 , 148.1,86.91 , 152.1,90.74 , 158.7,94.2 , 166.4,94.02 , 168.5,94.02 , 168.2,89.64 , 167.6,87.46 , 169.4,87.48 , 170.9,95.84 , 171.5,104.4 , 168.7,108.6 , 164,112.8 , 158,118.1 , 146.5,119.3 , 135,115.2 , 126.5,109.9 , 116.4,103.3 , 115.5,96.75 , 119.3,94.56 , 123.4,93.11 , 121.9,90.74 , 117.3,93.47 , 113.9,95.11 , 109.5,93.11 , 107.5,88.37 , 108.4,81.99 , 108.4,79.08 , 100.9,78.35 , 96.8,75.43 , 96,70.33 , 93.3,73.25 , 89.3,70.33 , 89.1,64.86 , 90,59.58 , 91.7,58.12 , 94.8,58.67 , 97.8,59.22 , 100.2,58.31 , 97.3,57.21 , 93.3,57.21 , 94.6,53.02 , 100.6,50.65 , 105.7,54.3 , 105.9,59.22 , 107.7,59.76 , 107.3,55.75 , 110.8,54.48 , 116.8,55.75 , 122.8,59.4 , 125.2,64.86 , 123.7,70.88 , 117.2,72.33 , 113.2,71.24 , 111.9,67.6 , 108.4,66.69 , 108.4,68.69 , 111.3,69.97 , 113.2,73.43 , 109.5,77.22 ]

#=================================================================================================

def scale_shape(shape, x_amp, y_amp, x_offset, y_offset):
    """ Amplify/attenuate and position a shape.
        First add the offset and then amplify the result.
    """
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])

    # Scale and position the x-coordinates of the shape to a width of 1.0 and
    # Re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = ( x_list[j] * x_amp )+ x_offset 
        new_shape.append( x_list[j] )
        y_list[j] = ( y_list[j] * y_amp ) + y_offset 
        new_shape.append( y_list[j] ) 
    return new_shape

def next_step(shape, x_offset):
    """ Re-position all limbs for next step.
    """
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])

    # Scale and position the x-coordinates of the shape to a width of 1.0 and
    # re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = x_list[j] + x_offset 
        new_shape.append( x_list[j] )
        #y_list[j] = ( y_list[j] * y_amp ) + y_offset 
        new_shape.append( y_list[j] ) 
    return new_shape


def draw_walker(indx):
    """ Draw entire body as a stick man.
    """
    # Draw the head shape in position.
    chart_1.create_oval(hips[indx]-12, hips[indx+1]-12,hips[indx]+12, hips[indx+1]+12, fill= "magenta", width = 1, tag = 'line_1')  
    chart_1.create_line(hips[indx], hips[indx+1], shoulder[indx], shoulder[indx+1], fill= "magenta", width = 4, tag = 'line_1') 
 
    chart_1.create_line(hips[indx], hips[indx+1], knee_a[indx], knee_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], knee_b[indx], knee_b[indx+1], fill= "green", width = 2, tag = 'line_1') 

    chart_1.create_line(knee_a[indx], knee_a[indx+1], heel_a[indx], heel_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(knee_b[indx], knee_b[indx+1], heel_b[indx], heel_b[indx+1], fill= "green", width = 2, tag = 'line_1') 

    chart_1.create_line(elbow_a[indx], elbow_a[indx+1], shoulder[indx], shoulder[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(elbow_b[indx], elbow_b[indx+1], shoulder[indx], shoulder[indx+1], fill= "green", width = 2, tag = 'line_1') 

    chart_1.create_line(elbow_a[indx], elbow_a[indx+1], wrist_a[indx], wrist_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(elbow_b[indx], elbow_b[indx+1], wrist_b[indx], wrist_b[indx+1], fill= "green", width = 2, tag = 'line_1') 
 
    # New head, hands and shoes.
    new_head = place_shape(clown_head, head[indx],  head[indx+1])
    chart_1.create_line(new_head, fill= "red", width = 4, tag = 'line_1') 

    new_hand_a = place_shape(a_hand, wrist_a[indx], wrist_a[indx+1]) 
    chart_1.create_line(new_hand_a, fill= "blue", width = 2, tag = 'line_1') 

    new_hand_b = place_shape(b_hand, wrist_b[indx], wrist_b[indx+1]) 
    chart_1.create_line(new_hand_b, fill= "green", width = 2, tag = 'line_1') 

    new_shoe_a = place_shape(a_shoe, heel_a[indx], heel_a[indx+1]) 
    chart_1.create_line(new_shoe_a, fill= "blue", width = 2, tag = 'line_1') 

    new_shoe_b = place_shape(b_shoe, heel_b[indx], heel_b[indx+1]) 
    chart_1.create_line(new_shoe_b, fill= "green", width = 2, tag = 'line_1') 


def place_shape(shape, x_pos, y_pos):
    """ Position a shape at a position given by coordinates x_pos, y_pos.
    """
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])

    # Scale and position the x and y coordinates of the shape to new positions and
    # re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = x_list[j] + x_pos 
        new_shape.append( x_list[j] )
        y_list[j] = y_list[j] + y_pos
        new_shape.append( y_list[j] ) 
    return new_shape


def advance_step(x_offset):
    """ Prior to each step the trajectory ofr eack joint must be advanced by one stride.
    """
    global hips, head, shoulder, knee_a, knee_b, heel_a, heel_b, toe_a, toe_b,\
           elbow_a, elbow_b, wrist_a, wrist_b, hand_a, hand_b
    hips = next_step(hips, x_offset)
    head = next_step(head, x_offset)
    shoulder = next_step(shoulder, x_offset)
    knee_a = next_step(knee_a, x_offset)
    knee_b = next_step(knee_b, x_offset)
    heel_a = next_step(heel_a, x_offset)
    heel_b = next_step(heel_b, x_offset)
    elbow_a = next_step(elbow_a, x_offset)
    elbow_b = next_step(elbow_b, x_offset)
    wrist_a = next_step(wrist_a, x_offset)
    wrist_b = next_step(wrist_b, x_offset)

#======================================================================
stride_len = hips[16] - hips[0] 
x_offset = 100.0
y_offset = -100.0
x_amp = 5.0
y_amp = 6.0

# Scale and position all limbs.
hips = scale_shape(hips, x_amp, y_amp, x_offset, y_offset)
head = scale_shape(head, x_amp, y_amp, x_offset, y_offset)
shoulder = scale_shape(shoulder, x_amp, y_amp, x_offset, y_offset)

knee_a = scale_shape(knee_a, x_amp, y_amp, x_offset, y_offset)
heel_a = scale_shape(heel_a, x_amp, y_amp, x_offset, y_offset)

elbow_a = scale_shape(elbow_a, x_amp, y_amp, x_offset, y_offset)
wrist_a = scale_shape(wrist_a, x_amp, y_amp, x_offset, y_offset)

knee_b = scale_shape(knee_b, x_amp, y_amp, x_offset, y_offset)
heel_b = scale_shape(heel_b, x_amp, y_amp, x_offset, y_offset)

elbow_b = scale_shape(elbow_b, x_amp, y_amp, x_offset, y_offset)
wrist_b = scale_shape(wrist_b, x_amp, y_amp, x_offset, y_offset)
# New head, hand and shoes.
clown_head = scale_shape(clown_head, 1.0, 1.0, -150.0, -65.0)
a_hand = scale_shape(hand, 1.0, 1.0, -10.0, -20.0)
b_hand = scale_shape(hand, 1.0, 1.0, -10.0, -20.0)
a_shoe = scale_shape(shoe, 1.5, 1.5, -50.0, -30.0)
b_shoe = scale_shape(shoe, 1.5, 1.5, -50.0, -30.0)

# Complete the first step.
for i in range(len(hips)/2):
    draw_walker(2*i)
    animdelay()

x_offset += stride_len*x_amp 
advance_step(x_offset)

# Complete the second step.
for i in range(len(hips)/2):
    draw_walker(2*i)
    animdelay()

advance_step(x_offset)
# Complete the third step.
for i in range(len(hips)/2):
    draw_walker(2*i)
    animdelay()

root.mainloop()
