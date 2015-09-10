"""
Program name: muybridge_interpolation_stick_man_running_1.py
Objective: Demontrate code for a Muybridge motion capture man running using
linear interpolation between major frames.

Keywords: canvas, muybridge, motion capture, interpolation, stick man, running
============================================================================79 
Comments: Strategy:
For any two adjacent positions along the trajectory of a joint, 
calculate intermediate positions (by linear interposaltion). 
Step to each of these positions in turn untill the destination position is reached,
then repeat the procedure for the next two image captured positions.
What next?
Reverse direction.
Adjust limb length. for example a baby will have shorter arms and legs.
Introduce a limp.
Adjust thigh to calf ratio.
Widen hips and narrow shoulders (female).

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine
"""
from Tkinter import *
import time
root = Tk()
root.title("Interpolated Runner.") 

cw = 1800                                   # canvas width
ch = 550                                    # canvas height
                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

cycle_period =70 # time between new positions of the ball (milliseconds).
def animdelay():
    chart_1.update()              # This refreshes the drawing on the canvas.
    chart_1.after(cycle_period)   # This makes execution pause for 100 milliseconds.
    chart_1.delete('line_1')      # This erases everything on the canvas.

#=======================================================================
# Stick-man running joint time-trajectories.  
#=======================================================================
head = [  192.1,1377 , 416.9,1375 , 527,1377 , 651.3,1381 , 761.4,1376 , 907.4,1374 , 997.9,1382 , 1090,1386 , 1211,1382 , 1335,1386 , 1468,1389 , 1588,1391 ]
neck = [  165.6,1405 , 391.5,1402 , 502.1,1410 , 627,1417 , 736,1414 , 879.9,1406 , 979.9,1404 , 1067,1408 , 1185,1405 , 1307,1411 , 1446,1410 , 1562,1416 ]

shoulder_a = [ 157.1,1436 , 368.5,1427 , 472.9,1442 , 605,1448 , 694.4,1442 , 843.7,1424 , 951,1425 , 1034,1431 , 1153,1442 , 1282,1453 , 1437,1451 , 1566,1445 ]
elbow_a = [ 198.7,1555 , 369.3,1553 , 434.7,1547 , 511.4,1535 , 588.1,1494 , 728.4,1425 , 826.1,1421 , 921.5,1455 , 1064,1514 , 1248,1578 , 1456,1573 , 1602,1559 ]
wrist_a = [ 266.8,1488 , 457.6,1532 , 517,1602 , 552.2,1647 , 597.1,1603 , 722.4,1527 , 820.5,1524 , 951.8,1565 , 1128,1601 , 1333,1610 , 1537,1544 , 1657,1506 ]
hand_a = [ 276.9,1471 , 472.5,1518 , 540.2,1612 , 560.8,1672 , 607.6,1626  , 730.3,1549 ,  827.6,1546 , 960.4,1581 , 1155,1610 , 1364,1610 , 1553,1530 , 1664,1482  ]

shoulder_b = [ 144.8,1414 , 366.6,1425 , 477.4,1429 , 605,1450 , 735.2,1455 , 893.8,1441 , 983.2,1445 , 1032,1436 , 1156,1447 , 1285,1456 , 1421,1442 , 1525,1445 ]
elbow_b = [ 49.01,1419 , 272.4,1460 , 403.7,1514 , 552.2,1560 , 707.5,1573 , 925.6,1544 , 1012,1549 , 1046,1551 , 1099,1548 , 1204,1549 , 1315,1493 , 1424,1458 ]
wrist_b = [ 83.06,1509 , 311.3,1543 , 458.7,1599 , 647.6,1626 , 819,1583 , 981.3,1487 , 1054,1486 , 1121,1546 , 1197,1611 , 1273,1623 , 1376,1580 , 1488,1536 ]
hand_b = [ 93.91,1526 , 323.2,1556 , 467.3,1613 , 666.3,1636 , 840.7,1575 , 988.1,1465 , 1053,1458 , 1139,1532 , 1216,1615 , 1284,1637 , 1399,1595 , 1502,1549 ]

hips = [  94.18,1637 , 308.5,1633 , 425.4,1634 , 560.3,1646 , 672,1649 , 830.7,1639 , 924.3,1643 , 1003,1638 , 1122,1648 , 1241,1649 , 1378,1655 , 1514,1648 ]

knee_a = [  26.46,1801 , 280.4,1808 , 451.3,1817 , 669.8,1789 , 838.1,1738 , 1007,1710 , 1092,1737 , 1138,1776 , 1216,1794 , 1285,1820 , 1337,1820 , 1432,1805 ]
heel_a = [ -173.3,1861 , 91.8,1751 , 270.6,1717 , 477.2,1737 , 639.4,1801 , 927,1890 , 1094,1941 , 1161,1972 , 1171,1988 , 1184,1993 , 1203,1960 , 1249,1896 ]
foot_a = [ -172.5,1917 , 60.32,1793 , 236.5,1760 , 455,1789 , 660.3,1854 , 977.8,1910 , 1163,1940 , 1211,1972 , 1241,1995 , 1242,1997 , 1246,1998 , 1260,1954 ]
toe_a = [ -163,1937 , 61.38,1818 , 229.6,1794 , 467.5,1826 , 685.2,1878 , 1016,1905 , 1184,1922 , 1243,1953 , 1263,1990 , 1277,2000 , 1282,1995 , 1289,1971 ]

knee_b = [ 284.7,1706 , 472.2,1746 , 544.7,1772 , 620.3,1808 , 644.6,1838 , 742.6,1796 , 847,1812 , 970.1,1820 , 1152,1823 , 1354,1806 , 1560,1739 , 1699,1722 ]
heel_b = [ 243.9,1897 , 475.9,1935 , 510.3,1975 , 515.6,1985 , 521.5,1971 , 577.3,1900 , 641.3,1830 , 801.4,1718 , 1003,1691 , 1179,1733 , 1388,1823 , 1616,1901 ]
foot_b = [ 310.5,1911 , 545.1,1938 , 570.2,1984 , 576.2,1994 , 589.3,1995 , 594.5,1957 , 634.5,1895 , 761.4,1769 , 957.4,1740 , 1154,1791 , 1413,1874 , 1676,1926 ]
toe_b = [ 328.5,1893 , 563.4,1921 , 597.9,1971 , 609.1,1996 , 613.9,1994 , 618.4,1970 , 651,1916 , 764,1793 , 958.1,1767 , 1168,1815 , 1438,1887 , 1701,1915 ]

#===================================================================================================
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


def subdivide_trajectory(num_steps, indx):
    """  The collection of trajectories will be handles as global variables for now.
    """
    global hips, head, shoulder_a, shoulder_b, knee_a, knee_b, heel_a, heel_b, foot_a, foot_b, toe_a, toe_b,\
           elbow_a, elbow_b, wrist_a, wrist_b, hand_a, hand_b

    dx_head = (head[indx+2]- head[indx])/num_steps  
    dy_head = (head[indx+3]- head[indx + 1])/num_steps  
    dx_neck = (neck[indx+2]- neck[indx ])/num_steps  
    dy_neck = (neck[indx+3]- neck[indx + 1])/num_steps  

    dx_shoulder_a = (shoulder_a[indx+2]- shoulder_a[indx])/num_steps  
    dy_shoulder_a = (shoulder_a[indx+1]- shoulder_a[indx + 3])/num_steps  
    dx_elbow_a = (elbow_a[indx+2]- elbow_a[indx])/num_steps  
    dy_elbow_a = (elbow_a[indx+3]- elbow_a[indx + 1])/num_steps   
    dx_wrist_a = (wrist_a[indx+2]- wrist_a[indx ])/num_steps  
    dy_wrist_a = (wrist_a[indx+3]- wrist_a[indx + 1])/num_steps  
    dx_hand_a = (hand_a[indx+2]- hand_a[indx ])/num_steps  
    dy_hand_a = (hand_a[indx+3]- hand_a[indx + 1])/num_steps 

    dx_shoulder_b = (shoulder_b[indx+2]- shoulder_b[indx])/num_steps  
    dy_shoulder_b = (shoulder_b[indx+3]- shoulder_b[indx + 1])/num_steps  
    dx_elbow_b = (elbow_b[indx+2]- elbow_b[indx ])/num_steps  
    dy_elbow_b = (elbow_b[indx+3]- elbow_b[indx + 1])/num_steps  
    dx_wrist_b = (wrist_b[indx+2]- wrist_b[indx ])/num_steps  
    dy_wrist_b = (wrist_b[indx+3]- wrist_b[indx + 1])/num_steps  
    dx_hand_b = (hand_b[indx+2]- hand_b[indx ])/num_steps  
    dy_hand_b = (hand_b[indx+3]- hand_b[indx + 1])/num_steps 

    dx_hips = (hips[indx+2]- hips[indx ])/num_steps  
    dy_hips = (hips[indx+3]- hips[indx + 1])/num_steps  

    dx_knee_a = (knee_a[indx+2]- knee_a[indx])/num_steps  
    dy_knee_a = (knee_a[indx+3]- knee_a[indx + 1])/num_steps 
    dx_heel_a = (heel_a[indx+2]- heel_a[indx ])/num_steps  
    dy_heel_a = (heel_a[indx+3]- heel_a[indx + 1])/num_steps  
    dx_foot_a = (foot_a[indx+2]- foot_a[indx ])/num_steps   
    dy_foot_a = (foot_a[indx+3]- foot_a[indx + 1])/num_steps   
    dx_toe_a = (toe_a[indx+2]- toe_a[indx ])/num_steps   
    dy_toe_a = (toe_a[indx+3]- toe_a[indx + 1])/num_steps   

    dx_knee_b = (knee_b[indx+2]- knee_b[indx ])/num_steps  
    dy_knee_b = (knee_b[indx+3]- knee_b[indx + 1])/num_steps 
    dx_heel_b = (heel_b[indx+2]- heel_b[indx ])/num_steps  
    dy_heel_b = (heel_b[indx+3]- heel_b[indx + 1])/num_steps  
    dx_foot_b = (foot_b[indx+2]- foot_b[indx ])/num_steps   
    dy_foot_b = (foot_b[indx+3]- foot_b[indx + 1])/num_steps   
    dx_toe_b = (toe_b[indx+2]- toe_b[indx ])/num_steps   
    dy_toe_b = (toe_b[indx+3]- toe_b[indx + 1])/num_steps
   
    return  dx_hips, dy_hips, dx_head, dy_head, dx_neck, dy_neck,\
            dx_shoulder_a, dy_shoulder_a, dx_elbow_a, dy_elbow_a, dx_wrist_a, dy_wrist_a, dx_hand_a, dy_hand_a,\
            dx_shoulder_b, dy_shoulder_b, dx_elbow_b, dy_elbow_b, dx_wrist_b, dy_wrist_b, dx_hand_b, dy_hand_b,\
            dx_knee_a, dy_knee_a, dx_heel_a, dy_heel_a, dx_foot_a, dy_foot_a, dx_toe_a, dy_toe_a,\
            dx_knee_b, dy_knee_b, dx_heel_b, dy_heel_b, dx_foot_b, dy_foot_b, dx_toe_b, dy_toe_b


def dxy_stepper(indx, num_steps):
    """  Draw the set of joints and limbs for an intermediate sinterpolation step,
    """
    #    dxy = subdivide_trajectory(num_steps, indx) 
    dxy = subdivide_trajectory(num_steps, indx) 
    """ Now we have the incremental coordinat changes between indices 
       and must now cyle through them for the number of steps num_steps - drawing the figure at each increment.
    """ 
    dx_hips       =  dxy[0]
    dy_hips       =  dxy[1] 
    dx_head       =  dxy[2]
    dy_head       =  dxy[3] 
    dx_neck       =  dxy[4]
    dy_neck       =  dxy[5]
    dx_shoulder_a =  dxy[6]
    dy_shoulder_a =  dxy[7]
    dx_elbow_a    =  dxy[8]
    dy_elbow_a    =  dxy[9] 
    dx_wrist_a    =  dxy[10]
    dy_wrist_a    =  dxy[11] 
    dx_hand_a     =  dxy[12]
    dy_hand_a     =  dxy[13]
    dx_shoulder_b =  dxy[14]
    dy_shoulder_b =  dxy[15] 
    dx_elbow_b    =  dxy[16]
    dy_elbow_b    =  dxy[17] 
    dx_wrist_b    =  dxy[18]
    dy_wrist_b    =  dxy[19] 
    dx_hand_b     =  dxy[20]
    dy_hand_b     =  dxy[21]
    dx_knee_a     =  dxy[22]
    dy_knee_a     =  dxy[23] 
    dx_heel_a     =  dxy[24]
    dy_heel_a     =  dxy[25] 
    dx_foot_a     =  dxy[26]
    dy_foot_a     =  dxy[27]
    dx_toe_a      =  dxy[28]
    dy_toe_a      =  dxy[29]
    dx_knee_b     =  dxy[30]
    dy_knee_b     =  dxy[31]
    dx_heel_b     =  dxy[32]
    dy_heel_b     =  dxy[33]
    dx_foot_b     =  dxy[34]
    dy_foot_b     =  dxy[35] 
    dx_toe_b      =  dxy[36]
    dy_toe_b      =  dxy[37]

    for i in range(num_steps):
        # Get new intermediate positions.
        ix_hips = hips[indx] + i*dx_hips
        iy_hips = hips[indx+1] + i*dy_hips 
        ix_head = head[indx] + i*dx_head
        iy_head = head[indx+1] + i*dy_head

        ix_shoulder_a = shoulder_a[indx] + i*dx_shoulder_a
        iy_shoulder_a = shoulder_a[indx+1] + i*dy_shoulder_a
        ix_elbow_a = elbow_a[indx] + i*dx_elbow_a
        iy_elbow_a = elbow_a[indx+1] + i*dy_elbow_a
        ix_wrist_a = wrist_a[indx] + i*dx_wrist_a
        iy_wrist_a = wrist_a[indx+1] + i*dy_wrist_a
        ix_hand_a = hand_a[indx] + i*dx_hand_a
        iy_hand_a = hand_a[indx+1] + i*dy_hand_a

        ix_knee_a = knee_a[indx] + i*dx_knee_a
        iy_knee_a = knee_a[indx+1] + i*dy_knee_a
        ix_heel_a = heel_a[indx] + i*dx_heel_a
        iy_heel_a = heel_a[indx+1] + i*dy_heel_a
        ix_foot_a = foot_a[indx] + i*dx_foot_a
        iy_foot_a = foot_a[indx+1] + i*dy_foot_a
        ix_toe_a = toe_a[indx] + i*dx_toe_a
        iy_toe_a = toe_a[indx+1] + i*dy_toe_a

        ix_shoulder_b = shoulder_b[indx] + i*dx_shoulder_b
        iy_shoulder_b = shoulder_b[indx+1] + i*dy_shoulder_b
        ix_elbow_b = elbow_b[indx] + i*dx_elbow_b
        iy_elbow_b = elbow_b[indx+1] + i*dy_elbow_b
        ix_wrist_b = wrist_b[indx] + i*dx_wrist_b
        iy_wrist_b = wrist_b[indx+1] + i*dy_wrist_b
        ix_hand_b = hand_b[indx] + i*dx_hand_b
        iy_hand_b = hand_b[indx+1] + i*dy_hand_b

        ix_knee_b = knee_b[indx] + i*dx_knee_b
        iy_knee_b = knee_b[indx+1] + i*dy_knee_b
        ix_heel_b = heel_b[indx] + i*dx_heel_b
        iy_heel_b = heel_b[indx+1] + i*dy_heel_b
        ix_foot_b = foot_b[indx] + i*dx_foot_b
        iy_foot_b = foot_b[indx+1] + i*dy_foot_b
        ix_toe_b = toe_b[indx] + i*dx_toe_b
        iy_toe_b = toe_b[indx+1] + i*dy_toe_b

        # Head, shoulders, hips
        chart_1.create_oval(ix_hips-12, iy_hips-12,ix_hips+12, iy_hips+12, fill= "magenta", width = 1, tag = 'line_1') 
        chart_1.create_oval(ix_head-12, iy_head-12,ix_head+12, iy_head+12, fill= "brown", width = 1, tag = 'line_1') 
        chart_1.create_line( ix_shoulder_a, iy_shoulder_a,  ix_shoulder_b, iy_shoulder_b, fill= "magenta", width = 8, tag = 'line_1') 
        chart_1.create_line(ix_hips, iy_hips, ix_shoulder_a, iy_shoulder_a, fill= "magenta", width = 4, tag = 'line_1') 
        chart_1.create_line(ix_hips, iy_hips, ix_shoulder_b, iy_shoulder_b, fill= "magenta", width = 4, tag = 'line_1') 

        chart_1.create_line(ix_hips, iy_hips, ix_knee_a, iy_knee_a, fill= "blue", width = 8, tag = 'line_1') 
        chart_1.create_line(ix_hips, iy_hips, ix_knee_b, iy_knee_b, fill= "green", width = 8, tag = 'line_1') 
        chart_1.create_line(ix_knee_a, iy_knee_a, ix_heel_a, iy_heel_a, fill= "blue", width = 2, tag = 'line_1') 
        chart_1.create_line(ix_knee_b, iy_knee_b, ix_heel_b, iy_heel_b, fill= "green", width = 2, tag = 'line_1') 
        chart_1.create_line(ix_foot_a, iy_foot_a, ix_heel_a, iy_heel_a, fill= "blue", width = 2, tag = 'line_1') 
        chart_1.create_line(ix_foot_b, iy_foot_b, ix_heel_b, iy_heel_b, fill= "green", width = 2, tag = 'line_1') 
        chart_1.create_oval( ix_toe_a-3, iy_toe_a-3,  ix_toe_a+3, iy_toe_a+3,fill= "blue", width = 2, tag = 'line_1') 
        chart_1.create_oval( ix_toe_b-3, iy_toe_b-3,  ix_toe_b+3, iy_toe_b+3,fill= "green", width = 2, tag = 'line_1') 

        chart_1.create_line(ix_elbow_a, iy_elbow_a, ix_shoulder_a, iy_shoulder_a, fill= "blue", width = 8, tag = 'line_1') 
        chart_1.create_line(ix_elbow_b, iy_elbow_b, ix_shoulder_b, iy_shoulder_b, fill= "green", width = 8, tag = 'line_1') 
        chart_1.create_line(ix_elbow_a, iy_elbow_a, ix_wrist_a, iy_wrist_a, fill= "blue", width = 2, tag = 'line_1') 
        chart_1.create_line(ix_elbow_b, iy_elbow_b, ix_wrist_b, iy_wrist_b, fill= "green", width = 2, tag = 'line_1') 
        chart_1.create_oval( ix_wrist_a-5, iy_wrist_a-5,  ix_wrist_a+5, iy_wrist_a+5,fill= "blue", width = 2, tag = 'line_1') 
        chart_1.create_oval( ix_wrist_b-5, iy_wrist_b-5,  ix_wrist_b+5, iy_wrist_b+5,fill= "green", width = 2, tag = 'line_1') 
        animdelay()

def advance_step(x_offset):
    """ Prior to each step the trajectory of each joint must be advanced by one stride.
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

#   Get interpolated positions. 
def get_delta(num_steps, xy_start, xy_end):
    """ Calculate the separate x and y axis increments between start and end
        coordinates xy_start and xy_end.
    """
    x_delta = (xy_end[0] - xy_start[0])/float(num_steps)
    y_delta = (xy_end[1] - xy_start[1])/float(num_steps)
    return x_delta, y_delta


#======================================================================
# Test and Demonstrate.
max_hips = len(hips) - 2
print 'max_hips:', max_hips
stride_len = hips[max_hips] - hips[0] 
print 'stride_len:', stride_len
x_offset = 0.0
y_offset = -100.0
x_amp = 0.2
y_amp = 0.2

def scale_locate_limbs(x_amp, y_amp, x_offset, y_offset):
    """ Scale and position all limbs.
    """
    global hips, head, neck, shoulder_a, shoulder_b, knee_a, knee_b, heel_a, heel_b, foot_a, foot_b, toe_a, toe_b,\
           elbow_a, elbow_b, wrist_a, wrist_b, hand_a, hand_b
    hips = scale_shape(hips, x_amp, y_amp, x_offset, y_offset)
    head = scale_shape(head, x_amp, y_amp, x_offset, y_offset)
    neck = scale_shape(neck, x_amp, y_amp, x_offset, y_offset)

    shoulder_a = scale_shape(shoulder_a, x_amp, y_amp, x_offset, y_offset)
    elbow_a = scale_shape(elbow_a, x_amp, y_amp, x_offset, y_offset)
    wrist_a = scale_shape(wrist_a, x_amp, y_amp, x_offset, y_offset)
    hand_a = scale_shape(hand_a, x_amp, y_amp, x_offset, y_offset)
    shoulder_b = scale_shape(shoulder_b, x_amp, y_amp, x_offset, y_offset)
    elbow_b = scale_shape(elbow_b, x_amp, y_amp, x_offset, y_offset)
    wrist_b = scale_shape(wrist_b, x_amp, y_amp, x_offset, y_offset)
    hand_b = scale_shape(hand_b, x_amp, y_amp, x_offset, y_offset)

    knee_a = scale_shape(knee_a, x_amp, y_amp, x_offset, y_offset)
    heel_a = scale_shape(heel_a, x_amp, y_amp, x_offset, y_offset)
    foot_a = scale_shape(foot_a, x_amp, y_amp, x_offset, y_offset)
    toe_a = scale_shape(toe_a, x_amp, y_amp, x_offset, y_offset)
    knee_b = scale_shape(knee_b, x_amp, y_amp, x_offset, y_offset)
    heel_b = scale_shape(heel_b, x_amp, y_amp, x_offset, y_offset)
    foot_b = scale_shape(foot_b, x_amp, y_amp, x_offset, y_offset)
    toe_b = scale_shape(toe_b, x_amp, y_amp, x_offset, y_offset)

#def extra_step(x_offset):
def extra_step():
    """ Draw one more step advanced by x_offset.
    """
    #advance_step(x_offset)
    # Complete the next step.
    for i in range(len(hips)/2):
        if 2*i <= len(hips)-3:
            dxy_stepper(2*i, num_steps) 

# Man # 1
#----------------
scale_locate_limbs(x_amp, y_amp, x_offset, y_offset)
x_offset += stride_len*x_amp 
# Complete the first step.
num_steps = 10
for i in range(len(hips)/2):
    # Generate sub-frames.   
    if 2*i <= len(hips)-3:
        dxy_stepper(2*i, num_steps) 

advance_step(x_offset)
extra_step()

advance_step(x_offset)
extra_step()

advance_step(x_offset)
extra_step()

advance_step(x_offset)
extra_step()

advance_step(x_offset)
extra_step()

root.mainloop()
