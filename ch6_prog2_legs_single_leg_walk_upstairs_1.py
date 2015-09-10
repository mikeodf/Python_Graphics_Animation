"""
Program name: legs_single_leg_walk_upstairs_1.py
Objective: Use only one pre-designed single heel trajectory. Derive the other leg
and hip trajectories from this. Make stride length and step height variable.

Keywords: canvas, legs, walking up stairs, single leg trajectory, arbitrary paths.
============================================================================79 
Comments: Assumptions: The left leg follows a similar trajectory to the right.
Hips are a fixed height above the heel (results in flawed thigh length).
 
Caveat: Calculate lists of knee positions prior to animation. This means that 
cpu expensive calculations are done once when the step size or height is changed.
This should allow the animations to proceed with a lower computational overhead. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import math
import time
import copy
root = Tk()
root.title("Legs Climbing.") 

cw = 1700                                   # canvas width
ch = 850                                   # canvas height
                             
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0, column=0)

cycle_period = 30 # time between new positions of the ball (milliseconds).
def animdelay():
    canvas_1.update()              # This refreshes the drawing on the canvas.
    canvas_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    canvas_1.delete('line_1')      # This erases everything on the canvas.

#======================================================================================================================
# Single leg trajectory: Ascending Stairs

heel_a = [ 173.5,2657 , 178.7,2646 , 182.9,2638 , 188.7,2625 , 194,2615   , 198.7,2604 , 201.7,2595 , 205.8,2582 , 209.6,2568 , 213.5,2554 ,
           216.5,2541 , 220,2527   , 224,2511   , 228.1,2494 , 232.3,2479 , 239,2461   , 250,2444   , 262.5,2430 , 279.4,2418 , 299.8,2406 , 
           321.2,2397 , 346.9,2390 , 373.5,2387 , 404.4,2390 , 425.4,2400 , 443.1,2413 , 455,2423   , 466,2434   , 478.3,2447 , 488.1,2456 , 
           494.6,2463 , 498.7,2473, 
498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473  , 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473 ]

# ======================================================================================

def zero_trajectory(heel_a):
    """ Translate/shift the trajectory to a start position where heel_a is a x=0, y=0.
        With a zero based trajectory other limb positions can be derived.
    """
    x_heel_a_start = heel_a[0]
    y_heel_a_start = heel_a[1]

    x_a =[]
    y_a =[]
    new_heel_a = []

    # Split the list into separate x and y lists. 
    for i in range(len(heel_a)/2):
        x_a.append(heel_a[2*i])
        y_a.append(heel_a[2*i + 1])

    # Shift all trajectories relative to heel_a start.
    for j in range(len(x_a)):  
        x_a[j] = x_a[j] - x_heel_a_start
        y_a[j] = y_a[j] - y_heel_a_start

    # Re-interleave shapes.
    for k in range(len(x_a)):
        new_heel_a.append(x_a[k])  
        new_heel_a.append(y_a[k])    
    return  new_heel_a


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

    # Amplify, add offsets and re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = ( x_list[j] * x_amp ) + x_offset 
        new_shape.append( x_list[j] )
        y_list[j] = ( y_list[j] * y_amp ) + y_offset 
        new_shape.append( y_list[j] ) 
    return new_shape

def draw_1position(indx):
    """ Draw entire body as a stick man.
    """
    global hips, heel_a, heel_b, knee_a, knee_b
    canvas_1.create_oval( hips[indx]-10,  hips[indx+1]-10, hips[indx]+10,  hips[indx+1]+10, fill= "magenta", width = 1, tag = 'line_1')  
    canvas_1.create_line( knee_a[indx],  knee_a[indx+1],  heel_a[indx],  heel_a[indx+1], fill= "red", width = 5, tag = 'line_1') 
    canvas_1.create_line( hips[indx],  hips[indx+1],  knee_a[indx],  knee_a[indx+1], fill= "blue", width = 10, tag = 'line_1') 
    canvas_1.create_line( knee_b[indx],  knee_b[indx+1],  heel_b[indx],  heel_b[indx+1], fill= "orange", width = 5, tag = 'line_1') 
    canvas_1.create_line( hips[indx],  hips[indx+1],  knee_b[indx],  knee_b[indx+1], fill= "green", width = 10, tag = 'line_1') 
    canvas_1.create_oval( knee_a[indx]-2,  knee_a[indx+1]-2, knee_a[indx]+2,  knee_a[indx+1]+2, fill= "blue", width = 1, tag = 'line_1')  
    canvas_1.create_oval( heel_a[indx]-2,  heel_a[indx+1]-4, heel_a[indx]+20,  heel_a[indx+1]+4, fill= "blue", width = 1, tag = 'line_1')  
    canvas_1.create_oval( heel_b[indx]-2,  heel_b[indx+1]-4, heel_b[indx]+20,  heel_b[indx+1]+4, fill= "green", width = 1, tag = 'line_1')  
    canvas_1.create_oval( knee_b[indx]-2,  knee_b[indx+1]-2, knee_b[indx]+2,  knee_b[indx+1]+2, fill= "green", width = 1, tag = 'line_1')  
 
def next_step(shape, x_offset, y_offset):
    """ Re-position all limbs by x_offset and y_offset in preparation for the next step.
        That is, advance the position of a whole shape by x_offset and y_offset.
    """
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])

    # Re-interleave the x and y components.
    for j in range(len(x_list)):
        x_list[j] = x_list[j] + x_offset
        y_list[j] = y_list[j] + y_offset 
        new_shape.append( x_list[j] )
        new_shape.append( y_list[j] ) 
    return new_shape


def walk_1stride(x_offset, y_offset, hips, knee_a, knee_b, heel_a, heel_b):
    """  Advance all related joint trajectories by one stride length, including
         the pre-created knee positions for the stride.         
    """
    # Reposition full trajectorie for next step (advance one stride).
    hips   = next_step(hips,   x_offset, y_offset)
    knee_a   = next_step(knee_a,   x_offset, y_offset)
    knee_b   = next_step(knee_b,   x_offset, y_offset)
    heel_b = next_step(heel_b, x_offset, y_offset) 
    heel_a = next_step(heel_a, x_offset, y_offset) 
    return hips, knee_a, knee_b, heel_a, heel_b

def show_static(hips, heel_a, heel_b, kula1, kula2, kula3):
    """ Draw the static trajectory.
    """ 
    # View them statically
    for i in range(len(hips)/2):
        canvas_1.create_oval( hips[i*2]-2,  hips[i*2+1]-2, hips[i*2]+2,  hips[i*2+1]+2, outline= kula1, fill= kula1, width = 1)  
        canvas_1.create_oval( heel_a[i*2]-2,  heel_a[i*2+1]-2, heel_a[i*2]+2,  heel_a[i*2+1]+2, outline= kula2, fill= kula2, width = 1)  
        canvas_1.create_oval( heel_b[i*2]-2,  heel_b[i*2+1]-2, heel_b[i*2]+2,  heel_b[i*2+1]+2, outline= kula3, fill= kula3, width = 1)  

def make_heel_hips(heel_a, leg_len_factor): # Manufacture the hip and heel_b position lists.
    """ Make hips and heel_b trajectories from heel_a trajectories.
        Each heel_a position will generate accompanying hip and heel_b positions.
        heel_a should be a zero referenced step trajectory. That is start at the origin.
        leg_len_factor gives leg_length to umodified step length (len_step).
    """
    #Get step length and height.
    len_step = heel_a[len(heel_a)-2] - heel_a[0]
    hite_step = heel_a[len(heel_a)-1] - heel_a[1]

    # Select leg length
    len_leg = leg_len_factor * len_step

    # Height of hips above heel start.
    x_hip_start = len_step/4
    y_hip_start = -math.sqrt(len_leg**2 - len_step**2/4)

    # Start location of heel_b.
    x_heel_b_start = len_step/2
    y_heel_b_start = hite_step/2

    x_hips =[]
    y_hips =[]
    x_heel_a =[]
    y_heel_a =[]
    x_heel_b =[]
    y_heel_b =[] 
    hips = []
    heel_b = []

    # Split the heel_a list into separate x and y lists. 
    for i in range(len(heel_a)/2):
        x_heel_a.append(heel_a[2*i])
        y_heel_a.append(heel_a[2*i + 1])
 
    # Generate heel_b trajectory.
    for j in range(len(heel_a)/2):    
        x_heel_b.append(heel_a[2*j] + len_step/2)
        y_heel_b.append(heel_a[2*j + 1] + hite_step/2)    

    # Swap first and second half of trajectory.
    """ This is because we need the static heel position of Heel_b to be
        at the start of the stride.
    """ 
    for n in range(len(x_heel_b)/2, len(x_heel_b)):   
        heel_b.append(x_heel_b[0])
        heel_b.append(y_heel_b[0])
    for n in range(0, len(x_heel_b)/2):   
        heel_b.append(x_heel_b[n])
        heel_b.append(y_heel_b[n])

    # Generate hips trajectory. This can be improved.
    x_increment = len_step * 2/len(heel_a)
    y_increment = hite_step * 2/len(heel_a)
    for k in range(len(heel_a)/2):    
        x_hips.append(x_hip_start + k*x_increment)
        y_hips.append(y_hip_start + k*y_increment)    

    # Reconstitute complete trajectories by interleaving. x- and y- lists.
    for m in range(len(heel_a)/2):     
        hips.append(x_hips[m])
        hips.append(y_hips[m])
    return hips, heel_b


def make_knee_lists(hips, heel_a, heel_b, thigh_leg_ratio):
    """ Each heel-hip position should generate an accompanying knee position.
        The knee position should be stored as lists like the hips and heel lists.
    """
    y_max = hips[1] - heel_b[1]
    x_max = hips[0] - heel_b[0]
    len_leg =  1.2 * math.sqrt( (y_max)**2 + (x_max)**2)  # For scaling thigh length. '1.2' suppresses straight-leg syndrome.
    len_thy = len_leg * thigh_leg_ratio
    len_calf = len_leg * (1 - thigh_leg_ratio)
    
    knee_a = []
    knee_b = []
    x_hips =[]
    y_hips =[]
    x_heel_a =[]
    y_heel_a =[]
    x_heel_b =[]
    y_heel_b =[]

    # Split the list into separate x and y lists. 
    for i in range(len(hips)/2):
        x_hips.append(hips[2*i])
        y_hips.append(hips[2*i + 1])
        x_heel_a.append(heel_a[2*i])
        y_heel_a.append(heel_a[2*i + 1])
        x_heel_b.append(heel_b[2*i])
        y_heel_b.append(heel_b[2*i + 1])

    for j in range(len(hips)/2):
        ax,ay = kneePosition(x_heel_a[j], y_heel_a[j], x_hips[j], y_hips[j], len_thy, len_calf)  
        bx,by = kneePosition(x_heel_b[j], y_heel_b[j], x_hips[j], y_hips[j], len_thy, len_calf)  
        knee_a.append(ax)
        knee_a.append(ay)
        knee_b.append(bx)
        knee_b.append(by)
    return knee_a, knee_b
    

def kneePosition(x_foot, y_foot, x_hip, y_hip, len_thy, len_calf):
    """ Law of cosines calculation to determine knee positions from hip and heel locations.
        Get knee position from hip and foot positions, thigh lengtha and thigh-to-calf ratio. 
        Arguments: foot position (x_foot,y_foot), hip position (x_hip, y_hip), thigh length (thy_len)
        thigh-to-calf ratio (thy_calf_ratio).
        Output (return variables): knee position.
    """
    ##theta_1 = -math.atan2((y_hip - y_foot), (x_hip - x_foot))   # Bad. 
    theta_1 = math.atan2((y_hip - y_foot), (x_hip - x_foot))   # Bend to right. Mammalian and Avian leg.
    #theta_1 = math.atan2((y_hip - y_foot), (x_foot - x_hip ))  # Bend to Left. Strange motion
    ##theta_1 = math.atan2((y_foot - y_hip ), (x_hip - x_foot))  # Bad solution.
    ##theta_1 = math.atan2((y_foot - y_hip ), (x_foot - x_hip ))  # Bad Solution.

    L1 = math.sqrt( (y_hip - y_foot)**2 + (x_hip - x_foot)**2)
    numerator = L1**2 + len_calf**2 - len_thy**2
    denominator = 2* L1 * len_calf
    asalpha   = numerator/denominator
    if L1 < len_thy + len_calf: # Limb not shorter than the distance from hip to heel.
        if denominator == 0.0:  alpha = math.pi   # Undesirable situation - infinity blowup.      
        if asalpha >= 1.0 : 
            alpha = 0.0           # a least harmful likely value.  
        elif asalpha <= -1.0 : alpha = math.pi    # a least harmful likely value. 
        if asalpha > -1.0 and asalpha < 1.0:          # Proper behavior.
            alpha = math.acos(asalpha) # Walking forwards, upward.
            #alpha = -math.acos(asalpha) # Walking backwards, downward.
    if L1 >= len_thy + len_calf: # Limb shorter than the distance from hip to heel.
        alpha = 0.0
    #beta =  theta_1 - alpha  # Avian motion
    beta =  theta_1 + alpha   # Mammalian motion.
    x_knee  = x_foot + len_calf * math.cos(beta)
    y_knee  = y_foot + len_calf * math.sin(beta)
    return x_knee, y_knee


def modify_linear_step(shape, add_fw, add_fh):
    """ Apply progressive linear addition to a trajectory shape.
        'add_fh' = 'added factor for step height'
        'add_fw' = 'added factor for step width' 
    """
    x_start = copy.deepcopy(shape[0])
    y_start = copy.deepcopy(shape[1])
    x_list =[]
    y_list =[]
    new_shape = []
    # Split the list into separate x and y lists. 
    for i in range(len(shape)/2):
        x_list.append(shape[2*i])
        y_list.append(shape[2*i + 1])
    # Shift all trajectories relative to heel_a start.
    for j in range(len(x_list)):  
        x_delta = x_list[j] - x_start # The horizontal distance from the start of the shape.
        y_delta = x_delta * add_fh    # The extra bit added to vertical components.
        x_list[j] = x_list[j] + x_delta * add_fw
        y_list[j] = y_list[j] - y_delta
    # Re-interleave shapes.
    for k in range(len(x_list)):
        new_shape.append(x_list[k])  
        new_shape.append(y_list[k])     
    return new_shape

def modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite):
    """ Apply progressive linear addition to a set of trajectory shapes.
        'add_fh' = 'added factor for step height'
        'add_fw' = 'added factor for step width' 
    """
    hips   = modify_linear_step(hips,   add_fwidth, add_fhite)
    heel_a = modify_linear_step(heel_a, add_fwidth, add_fhite)
    heel_b = modify_linear_step(heel_b, add_fwidth, add_fhite)
    return hips, heel_a, heel_b


def leg_geometry(hips, heel_a, heel_b, thigh_leg_ratio):
    """ Calculate leg, thigh and calf lengths for current trajectories.
        Return step length, step height, leg, thigh and calf lengths.
    """
    y_max = hips[1] - heel_b[1]
    x_max = hips[0] - heel_b[0]
    len_leg =  1.2 * math.sqrt( (y_max)**2 + (x_max)**2)  # For scaling thigh length. '1.2' suppresses straight-leg syndrome.
    len_thy = len_leg * thigh_leg_ratio
    len_calf = len_leg * (1 - thigh_leg_ratio)
    len_step = heel_a[len(heel_a)-2] - heel_a[0]
    hite_step = (heel_a[len(heel_a)-1] - heel_a[1])
    return len_step, hite_step, len_leg, len_thy, len_calf

#======================================================================
# Test and Demonstrate
#======================

heel_a = zero_trajectory(heel_a)  # Shift the heel_a trajectory to the origin of coordinates.
hips, heel_b = make_heel_hips(heel_a, 1.7) # *** leg_len_factor *******
# First maneuver them onto the screen.
x_amp = 0.5
y_amp = 0.4
x_offset = 0
y_offset = 800

# Place the trajectories at a suitable starting point.
hips = scale_shape(hips,       x_amp, y_amp, x_offset, y_offset )
heel_a = scale_shape(heel_a,   x_amp, y_amp, x_offset, y_offset )
heel_b = scale_shape(heel_b,   x_amp, y_amp, x_offset, y_offset )
knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.

# First step.
for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()

show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Second step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
add_fwidth = 0.3  # Per unit addition to step length.
add_fhite = 0.0   # Per unit addition to step height.
hips, heel_a, heel_b = modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite)

knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Third step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get new step length.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Fourth step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
add_fwidth = 0.0  # Per unit addition to step length.
add_fhite = 0.8   # Per unit addition to step height.
hips, heel_a, heel_b = modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite)

knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Fifth step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
add_fwidth = 0.0  # Per unit addition to step length.
add_fhite = -1.8   # Per unit addition to step height.
hips, heel_a, heel_b = modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite)
#len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.

knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Sixth step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
add_fwidth = 1.2  # Per unit addition to step length.
add_fhite = 0.1   # Per unit addition to step height.
hips, heel_a, heel_b = modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite)

knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Seventh step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
add_fwidth = -1.2  # Per unit addition to step length.
add_fhite = 0.1   # Per unit addition to step height.
hips, heel_a, heel_b = modify_shapes(hips, heel_a, heel_b,   add_fwidth,  add_fhite)

knee_a, knee_b = make_knee_lists(hips, heel_a, heel_b, 0.55)  # Last argument is thigh_leg_ratio.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)

for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')


# Eigth step.
len_step, hite_step, len_leg, len_thy, len_calf = leg_geometry(hips, heel_a, heel_b, 0.55) # Get old step length.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)
for i in range((len(hips)/2)):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# Ninth step.
hips, knee_a, knee_b, heel_a, heel_b = walk_1stride(len_step, hite_step, hips, knee_a, knee_b, heel_a, heel_b)
for i in range((len(hips)/2)-1):
    draw_1position(2*i)
    # Draw tracer trajectories.
    if 2*i+2 < len(hips):
        canvas_1.create_line( hips[2*i],  hips[2*i+1],  hips[2*i+2],  hips[2*i+3], fill = "#ffbbff", width = 1) 
        canvas_1.create_line( heel_a[2*i],  heel_a[2*i+1],  heel_a[2*i+2],  heel_a[2*i+3], fill = "#bbbbff", width = 1) 
        canvas_1.create_line( heel_b[2*i],  heel_b[2*i+1],  heel_b[2*i+2],  heel_b[2*i+3], fill = "#66ff66", width = 1) 
    animdelay()
print 'i:', i
draw_1position(2*i)  
show_static(hips, heel_a, heel_b, '#dd88dd', '#8888dd', '#88dd88')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

root.mainloop()
