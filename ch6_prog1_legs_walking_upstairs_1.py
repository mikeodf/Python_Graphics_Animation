"""
Program name: legs_walking_upstairs_1.py
Objective: Animate a rudimentary walking upstairs stride.

Keywords: canvas, legs, walking up stairs
============================================================================79 
Comments: Stride trajectories for a leg-figure ascending stairs were created.
The trajectories are only for hips and heels. Knees are generated using the cosine rule.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import math
import time
import copy
root = Tk()
root.title("Legs Moving Upstairs.") 

cw = 1000                                   # canvas width
ch = 700                                   # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period = 20 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 200 milliseconds.
    chart_1.delete('line_1')     # This erases everything on the canvas.

#======================================================================================================================
# Designer limb trajectories: Ascending Stairs
#==============================================

hips = [ 243.5,2190 , 248.8,2187 , 255.2,2184 , 261.1,2180 , 266.3,2178 , 271.7,2174 , 276.6,2172 , 282.7,2169 , 288.7,2166 , 293.6,2163 , 297.8,2160 , 298.5,2160 , 299.2,2160  , 303.2,2158 , 307.3,2155 , 311.8,2153 , 317,2150 , 322,2147 , 326.8,2145 , 330.8,2143 , 335.9,2140 , 340.6,2137 , 346.5,2134 , 350.7,2132 , 356,2129 , 361.3,2126 , 366.5,2123 , 371.6,2120 , 376.8,2118 , 382.2,2115 , 387.8,2112 , 392.2,2109 , 397.2,2107 , 401.1,2104 , 406.5,2102 , 411.9,2099 , 416.9,2096 , 423,2093 , 427.8,2090 , 432.6,2088 , 437.9,2085 , 443.2,2082 , 448.7,2079 , 453.8,2076 , 458.5,2073 , 462.6,2071 , 467.4,2069 , 472.1,2066 , 477.2,2063 , 482.2,2060 , 487.6,2058 , 492,2056 , 497,2052 , 502.7,2050 , 507.3,2047 , 512.7,2044 , 517.5,2041 , 523.9,2038 , 528.6,2035 , 533.7,2033 , 538.6,2030 , 544.6,2027 , 549.6,2024 , 554.9,2021 , 559.2,2019 , 564.6,2016 ]

heel_a = [ 173.5,2657 , 178.7,2646 , 182.9,2638 , 188.7,2625 , 194,2615 , 198.7,2604 , 201.7,2595 , 205.8,2582 , 209.6,2568 , 213.5,2554 , 216.5,2541 , 220,2527 , 224,2511 , 228.1,2494 , 232.3,2479 , 239,2461 , 250,2444 , 262.5,2430 , 279.4,2418 , 299.8,2406 , 321.2,2397 , 346.9,2390 , 373.5,2387 , 404.4,2390 , 425.4,2400 , 443.1,2413 , 455,2423 , 466,2434 , 478.3,2447 , 488.1,2456 , 494.6,2463 , 498.7,2473 
, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473  , 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473, 498.7,2473 , 498.7,2473, 498.7,2473 ]

heel_b = [  333.4,2567 ,333.4,2567 , 333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 , 333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 , 333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 , 333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,333.4,2567 ,
333.4,2567 , 338.6,2556 , 342.8,2548 , 348.6,2535 , 353.9,2525 , 358.6,2514 , 361.6,2505 , 365.7,2492 , 369.5,2478 , 373.4,2464 , 376.4,2451 , 379.9,2437 , 383.9,2421 , 388,2404 , 392.2,2389 , 398.9,2371 , 409.9,2354 , 422.4,2340 , 439.3,2328 , 459.7,2316 , 481.1,2307 , 506.8,2300 , 533.4,2297 , 564.3,2300 , 585.3,2310 , 603,2323 , 614.9,2333 , 625.9,2344 , 638.2,2357 , 648,2366 , 654.5,2373 , 658.6,2383 
  ]
# ======================================================================================

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
    chart_1.create_oval( hips[indx]-6,  hips[indx+1]-6, hips[indx]+6,  hips[indx+1]+6, fill= "magenta", width = 1, tag = 'line_1') 

    #chart_1.create_line( hips[indx],  hips[indx+1],  heel_a[indx],  heel_a[indx+1], fill= "grey", width = 1, tag = 'line_1') 
    chart_1.create_line( knee_a[indx],  knee_a[indx+1],  heel_a[indx],  heel_a[indx+1], fill= "red", width = 1, tag = 'line_1') 
    chart_1.create_line( hips[indx],  hips[indx+1],  knee_a[indx],  knee_a[indx+1], fill= "blue", width = 1, tag = 'line_1') 
    chart_1.create_line( knee_b[indx],  knee_b[indx+1],  heel_b[indx],  heel_b[indx+1], fill= "pink", width = 1, tag = 'line_1') 
    chart_1.create_line( hips[indx],  hips[indx+1],  knee_b[indx],  knee_b[indx+1], fill= "green", width = 1, tag = 'line_1') 

    chart_1.create_oval( knee_a[indx]-2,  knee_a[indx+1]-2, knee_a[indx]+2,  knee_a[indx+1]+2, fill= "blue", width = 1, tag = 'line_1')  
    chart_1.create_oval( heel_a[indx]-4,  heel_a[indx+1]-4, heel_a[indx]+4,  heel_a[indx+1]+4, fill= "blue", width = 1, tag = 'line_1')  
    chart_1.create_oval( heel_b[indx]-4,  heel_b[indx+1]-4, heel_b[indx]+4,  heel_b[indx+1]+4, fill= "green", width = 1, tag = 'line_1')  
    chart_1.create_oval( knee_b[indx]-2,  knee_b[indx+1]-2, knee_b[indx]+2,  knee_b[indx+1]+2, fill= "green", width = 1, tag = 'line_1')  
 
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



def walk_1stride(x_offset, y_offset, hips, heel_a, heel_b, thy_len, thy_calf_ratio ):
    """  Advance all related joint trajectories by one stride length,
         and create the list of knee poistions for the stride.
         Tests: Works without knee calcs.
    """
    # Reposition full trajectorie for next step (advance one stride).
    hips   = next_step(hips,   x_offset, y_offset)
    heel_b = next_step(heel_b, x_offset, y_offset) 
    heel_a = next_step(heel_a, x_offset, y_offset) 
    # Now generate the accompanying knee position lists.
    
    knee_a = []
    knee_b = []
    for j in range(len(hips)/2):
        x_knee_a, y_knee_a = kneePosition(heel_a[2*j], heel_a[2*j+1], hips[2*j], hips[2*j+1], thy_len, thy_calf_ratio)
        knee_a.append(x_knee_a)
        knee_a.append(y_knee_a)    
        x_knee_b, y_knee_b = kneePosition(heel_b[2*j], heel_b[2*j+1], hips[2*j], hips[2*j+1], thy_len, thy_calf_ratio)
        knee_b.append(x_knee_b)
        knee_b.append(y_knee_b)
    return knee_a, knee_b, hips, heel_a, heel_b
    
    #return hips, heel_a, heel_b

def kneePosition(x_foot, y_foot, x_hip, y_hip, len_thy, len_calf):
    """ Law of cosines calculation to determine knee positions from hip and heel locations.
        Get knee position from hip and foot positions, thigh lengtha and thigh-to-calf ratio. 
        Arguments: foot position (x_foot,y_foot), hip position (x_hip, y_hip), thigh length (thy_len)
        thigh-to-calf ratio (thy_calf_ratio).
        Output (return variables): knee position.
    """
    theta_1 = math.atan2((y_hip - y_foot), (x_hip - x_foot))   # Mammalian and Avian leg.
    #theta_1 = math.atan2((y_hip - y_foot), (x_foot - x_hip ))  # Strange motion
    #theta_1 = math.atan2((y_foot - y_hip ), (x_hip - x_foot))  # Bad solution.
    #theta_1 = math.atan2((y_foot - y_hip ), (x_foot - x_hip ))  # Bad Solution.

    L1 = math.sqrt( (y_hip - y_foot)**2 + (x_hip - x_foot)**2)
    numerator = L1**2 + len_calf**2 - len_thy**2
    denominator = 2* L1 * len_calf
    
    if L1 < len_thy + len_calf: # Limb nor shorter than the distance from hip to heel.
        if denominator == 0 : denominator = 0.0000001  # Deafault to one million - this will give acceptable values for alpha.
        alpha = math.acos(numerator/denominator) 
    else:
        alpha = 0.001 # Small angle for a minimum bend of the kne
    #beta =  theta_1 - alpha  # Avian motion
    beta =  theta_1 + alpha   # Mammalian motion.
    x_knee  = x_foot + len_calf * math.cos(beta)
    y_knee  = y_foot + len_calf * math.sin(beta)
    return x_knee, y_knee

def walk_arbitrary_step(x_offset, y_offset, hips, heel_a, heel_b, thy_len, thy_calf_ratio ):
    """  Advance all related joint trajectories by one stride length,
         and create the list of knee poistions for the stride.
         Tests: Works without knee calcs.
    """
    # Reposition fractional trajectory for next step (advance fractional stride).
    x_delta = x_offset*2/len(hips)
    y_delta = y_offset*2/len(hips)
    knee_a = []
    knee_b = []
    for j in range(0, len(hips),2):
        # For each slice the height will be proportionately raised.
        hips, heel_a, heel_b = fractional_stride(j, x_delta, y_delta, hips, heel_a, heel_b, thy_len, thy_calf_ratio ) 
        x_knee_a, y_knee_a = kneePosition(heel_a[j], heel_a[j+1], hips[j], hips[j+1], thy_len, thy_calf_ratio)  
        x_knee_b, y_knee_b = kneePosition(heel_b[j], heel_b[j+1], hips[j], hips[j+1], thy_len, thy_calf_ratio)
        knee_a.append(x_knee_a)
        knee_a.append(y_knee_a)    
        knee_b.append(x_knee_b)
        knee_b.append(y_knee_b)

    return knee_a, knee_b, hips, heel_a, heel_b
#======================================================================
# Test and Demonstrate
#======================
x_offset = -100.0
y_offset = 00.0
x_amp = 0.3
y_amp = 0.3

step_height = heel_b[1] - heel_a[1]

# Leg length and thigh-to-calf ratio.
y_max = hips[1] - heel_b[1]
x_max = hips[0] - heel_b[0]
len_leg =  1.2 * math.sqrt( (y_max)**2 + (x_max)**2)  # To be used for scaling thigh length.
thy_leg_ratio = 0.45
len_thy = len_leg * thy_leg_ratio
len_calf = len_leg * (1 - thy_leg_ratio)

# Scaled values for limbs.
len_thy_1 = len_thy * y_amp
len_calf_1 = len_calf * y_amp
hips = scale_shape(hips, x_amp, y_amp, x_offset, y_offset)
heel_a = scale_shape(heel_a, x_amp, y_amp, x_offset, y_offset)
heel_b = scale_shape(heel_b, x_amp, y_amp, x_offset, y_offset)
stride_len = heel_a[len(heel_a)-2] - heel_a[0]  # Length of stride after scaling.
y_heel_a_min = min(heel_a)
y_heel_b_min = min(heel_b)
step_height = y_heel_b_min - y_heel_a_min 

# Fresh trajectories.
knee_a, knee_b, hips, heel_a, heel_b = walk_1stride(x_offset, 0.0, hips, heel_a, heel_b, len_thy_1, len_calf_1 )
x_offset = stride_len
y_offset = -step_height * 1.1  # The 1.1 is to compensate for a heel_b slip, not currently understood.

for i in range((len(hips)/2)):
    draw_1position(2*i)
    animdelay()

for j in range(16):
    knee_a, knee_b, hips, heel_a, heel_b = walk_1stride(x_offset, y_offset, hips, heel_a, heel_b, len_thy_1, len_calf_1 )
    for i in range((len(hips)/2)):
        draw_1position(2*i)
        animdelay()

root.mainloop()
