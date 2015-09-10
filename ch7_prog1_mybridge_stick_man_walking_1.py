"""
Program name:muybridge stick_man_walking_1.py
Objective: Demontrate animation code for stick man trajectories to produce motion animation.

Keywords: canvas, stick man, walking, animation
============================================================================79 
Comments: Use the time trajectories of joint positions captured from 
photographic images to create animated walking movement..

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import time
root = Tk()
root.title("stick Man Walking.") 

cw = 1800                                   # canvas width
ch = 550                                    # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period =200 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 100 milliseconds.
    chart_1.delete('line_1')      # This erases everything on the canvas.

#=======================================================================
# Stick-man walker joint time-trajectories.  
#=======================================================================
head = [ 203.6,86.9 , 268,80.6 , 319.1,85.5 , 373,82 , 420,84.1 , 466.3,79.9 , 518.7,82.7 , 581.5,80.6 , 634.7,84.8 , 686.2,80.6 , 734.3,82.7 , 778.7,80.6 ]

neck = [ 206.4,108.6 , 267.3,104.4 , 321.2,106.5 , 373.7,106.5 , 432.1,101.6 , 482.7,96.7 , 520.7,103.7 , 580.1,104.4 , 637.6,105.8 , 688.6,106.5 , 746.2,100.9 , 794.5,96.7 ]
#.............................................................................
shoulder_a = [ 215.5,120.5 , 272.2,118.4 , 335.2,121.9 , 402.4,121.2 , 463.7,106.5 , 503.1,103 , 518.4,114.2 , 574,121.2 , 632.1,123.3 , 673.6,120.5 , 723.4,114.9 , 773,107.9 ]

elbow_a = [ 247.7,165.3 , 269.4,200.3 , 284.8,196.1 , 304.4,170.2 , 335.9,143.6 , 375.1,138.7 , 478.4,182.1 , 601.6,196.1 , 699.3,198.9 , 780.4,168.1 , 845.5,129.6 , 882.4,114.9 ]

wrist_a = [ 291.1,158.3, 332.4,240.9 ,  307.2,268.9 ,297.4,245.1 ,314.9,210.8 , 360.4,199.6 , 501.2,243 ,660.1,254.2 ,766.9,215 ,826.7,138.7 ,847.9,86.2 , 854.4,75.7 ]

hand_a = [ 292.5,147.1 , 350.6,240.9 , 320.5,281.5 , 304.4,258.4 , 319.1,230.4 , 365.3,217.1 , 514.2,254.9 , 673.4,260.5 , 781.1,211.5 , 833.8,127.5 , 841.6,72.9 , 838.5,71.5 ]
#.............................................................................
shoulder_b = [ 205,119.1 , 261,120.5 , 316.3,124 , 360.4,122.6 , 409.4,114.9 , 453.1,107.9 , 528.8,115.6 , 584.7,121.2 , 650.6,122.6 , 716.5,119.8 , 777.8,106.5 , 817,103.7 ]

elbow_b = [ 165.1,185.6 , 289.7,195.4 , 384.2,200.3 , 466.3,168.8 , 531.1,130.3 , 570,114.2 , 562.8,161.8 , 582.6,201 , 601.1,196.1 , 619.2,167.4 , 649.4,143.6 , 688,140.1 ]       

wrist_b = [ 186.8,246.5 , 347.1,253.5 , 450.2,216.4 , 512.1,140.1 , 534.3,87.6 , 541.1,74.3 , 605.4,154.8 , 646,241.6 , 622.3,268.2 , 611.4,243 , 629.6,208.7 , 673,201 ]

hand_b = [ 200.8,259.1 , 361.1,260.5 , 465.2,212.9 , 519.6,128.9 , 527.6,73.6 , 525,70.1 , 607.4,142.9 , 663.2,240.9 , 635.6,280.8 , 620,257.7 , 634.2,229.7 , 678.2,218.5 ]
#.............................................................................
hips = [ 256.8,255.6 , 318.4,251.4 , 354.8,261.9 , 412.9,262.6 , 461.5,264.7 , 512.4,255.6 , 571.8,250 , 631.6,250 , 671.6,263.3 , 725.7,259.8 , 777.5,264 , 825.9,256.3 ]

knee_a = [ 213.4,383 , 334.5,378.8 , 436.9,364.1 , 512.7,343.1 , 573.7,339.6 , 616.6,345.9 , 656.9,347.3 , 687.4,361.3 , 709,375.3 , 716.8,375.3 , 733.5,367.6 , 770.7,366.2 ]

heel_a = [ 83.9,427.1 , 207.8,434.1 , 334.5,462.8 , 481.6,479.6 , 597.9,471.2 , 624.4,483.1 , 623.8,485.2 , 624.9,483.8 , 625.2,480.3 , 624.9,477.5 , 628.4,471.2 , 643.4,436.9]

foot_a = [ 97.2,468.4 , 227.4,462.8 , 372.3,481.7 , 519.6,478.2 , 635.6,464.9 , 665.2,474.7 , 667.6,484.5 , 666.7,486.6 , 668.1,484.5 , 668.1,482.4 , 669.3,479.6 , 670.7,476.8 ]

toe_a = [ 120.3,481 , 251.2,476.8 , 395.4,485.2 , 544.1,466.3 , 647.7,451.6 , 679.7,460.7 , 686.9,483.1 , 686.9,485.2 , 686.6,488 , 688.6,487.3 , 688.6,485.9 , 688.8,483.8 ]
#.............................................................................
knee_b = [ 342.2,351.5 , 374.4,360.6 , 394,376 , 403.1,376 , 420,366.9 , 457.4,365.5 , 528.5,378.8 , 647.7,380.2 , 752.5,364.1 , 826.8,341.7 , 889,339.6 , 929.6,346.6 ]

heel_b = [ 309.3,489.4 , 309.3,488 , 309.3,485.9 , 309.3,483.8 , 313.5,471.2 , 330.3,436.2 , 398.2,423.6 , 521.3,434.8 , 649.3,462.1 , 795,477.5 , 912.1,471.2 , 938,485.2 ]

toe_b = [ 374.4,482.4 , 374.4,484.5 , 374.4,485.9 , 373,486.6 , 373,484.5 , 373.7,483.1 , 434.2,476.8 , 564,476.8 , 710.9,483.8 , 859,464.9 , 961.6,450.9 , 993.5,461.4 ]

foot_b = [  354.1,490.1,  354.1,488.7 , 353.4,488 , 353.4,486.6 ,354.1,485.9 , 357.6,475.4 ,412.2,464.2 ,539.7,464.2 ,687.6,481 ,   832,477.5 , 950.1,464.9 , 980,476.8   ]
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
    chart_1.create_oval(head[indx]-20, head[indx+1]-20, head[indx]+20, head[indx+1]+20,fill= "brown", width = 2, tag = 'line_1') 
    chart_1.create_oval(hips[indx]-12, hips[indx+1]-12,hips[indx]+12, hips[indx+1]+12, fill= "magenta", width = 1, tag = 'line_1')  

    chart_1.create_line( shoulder_a[indx], shoulder_a[indx+1], shoulder_b[indx], shoulder_b[indx+1], fill= "magenta", width = 4, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], shoulder_a[indx], shoulder_a[indx+1], fill= "magenta", width = 4, tag = 'line_1') 
 
    chart_1.create_line(hips[indx], hips[indx+1], shoulder_b[indx], shoulder_b[indx+1], fill= "magenta", width = 4, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], knee_a[indx], knee_a[indx+1], fill= "blue", width = 5, tag = 'line_1') 
    chart_1.create_line(hips[indx], hips[indx+1], knee_b[indx], knee_b[indx+1], fill= "green", width = 5, tag = 'line_1') 

    chart_1.create_line(knee_a[indx], knee_a[indx+1], heel_a[indx], heel_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(knee_b[indx], knee_b[indx+1], heel_b[indx], heel_b[indx+1], fill= "green", width = 2, tag = 'line_1') 
    chart_1.create_line(foot_a[indx], foot_a[indx+1], heel_a[indx], heel_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(foot_b[indx], foot_b[indx+1], heel_b[indx], heel_b[indx+1], fill= "green", width = 2, tag = 'line_1') 
    chart_1.create_oval( toe_a[indx]-6, toe_a[indx+1]-6,  toe_a[indx]+6, toe_a[indx+1]+10,fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_oval( toe_b[indx]-6, toe_b[indx+1]-6,  toe_b[indx]+6, toe_b[indx+1]+10,fill= "green", width = 2, tag = 'line_1') 

    chart_1.create_line(elbow_a[indx], elbow_a[indx+1], shoulder_a[indx], shoulder_a[indx+1], fill= "blue", width = 5, tag = 'line_1') 
    chart_1.create_line(elbow_b[indx], elbow_b[indx+1], shoulder_b[indx], shoulder_b[indx+1], fill= "green", width = 5, tag = 'line_1') 
    chart_1.create_line(elbow_a[indx], elbow_a[indx+1], wrist_a[indx], wrist_a[indx+1], fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_line(elbow_b[indx], elbow_b[indx+1], wrist_b[indx], wrist_b[indx+1], fill= "green", width = 2, tag = 'line_1') 
    chart_1.create_oval( wrist_a[indx]-10, wrist_a[indx+1]-10,  wrist_a[indx]+10, wrist_a[indx+1]+10,fill= "blue", width = 2, tag = 'line_1') 
    chart_1.create_oval( wrist_b[indx]-10, wrist_b[indx+1]-10,  wrist_b[indx]+10, wrist_b[indx+1]+10,fill= "green", width = 2, tag = 'line_1') 
 

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
    global hips, head, shoulder_a, shoulder_b, knee_a, knee_b, heel_a, heel_b, foot_a, foot_b, toe_a, toe_b,\
           elbow_a, elbow_b, wrist_a, wrist_b, hand_a, hand_b
    hips = next_step(hips, x_offset)
    head = next_step(head, x_offset)
    shoulder_a = next_step(shoulder_a, x_offset)
    shoulder_b = next_step(shoulder_b, x_offset)
    knee_a = next_step(knee_a, x_offset)
    knee_b = next_step(knee_b, x_offset)
    heel_a = next_step(heel_a, x_offset)
    heel_b = next_step(heel_b, x_offset)
    foot_a = next_step(foot_a, x_offset)
    foot_b = next_step(foot_b, x_offset)
    toe_a = next_step(toe_a, x_offset)
    toe_b = next_step(toe_b, x_offset)
    elbow_a = next_step(elbow_a, x_offset)
    elbow_b = next_step(elbow_b, x_offset)
    wrist_a = next_step(wrist_a, x_offset)
    wrist_b = next_step(wrist_b, x_offset)
    hand_a = next_step(hand_a, x_offset)
    hand_b = next_step(hand_b, x_offset)

#======================================================================
max_hips = len(hips) -2
stride_len = max_hips - hips[0]
stride_len = hips[22] - hips[0] 
x_offset = 0.0
y_offset = 0.0
x_amp = 1.0
y_amp = 1.0

# Scale and position all limbs.
hips = scale_shape(hips, x_amp, y_amp, x_offset, y_offset)
head = scale_shape(head, x_amp, y_amp, x_offset, y_offset)
shoulder_a = scale_shape(shoulder_a, x_amp, y_amp, x_offset, y_offset)
shoulder_b = scale_shape(shoulder_b, x_amp, y_amp, x_offset, y_offset)
knee_a = scale_shape(knee_a, x_amp, y_amp, x_offset, y_offset)
heel_a = scale_shape(heel_a, x_amp, y_amp, x_offset, y_offset)
elbow_a = scale_shape(elbow_a, x_amp, y_amp, x_offset, y_offset)
wrist_a = scale_shape(wrist_a, x_amp, y_amp, x_offset, y_offset)
knee_b = scale_shape(knee_b, x_amp, y_amp, x_offset, y_offset)
heel_b = scale_shape(heel_b, x_amp, y_amp, x_offset, y_offset)
elbow_b = scale_shape(elbow_b, x_amp, y_amp, x_offset, y_offset)
wrist_b = scale_shape(wrist_b, x_amp, y_amp, x_offset, y_offset)

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
