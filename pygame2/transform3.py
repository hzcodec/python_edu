#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-16
#   File        : transform3.py
#   Reference   : -
#   Description : Rotate a rectangle.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import math
import time

SIZE   = 800,600
COORDx = 200
COORDy = 100
RED    = [255,0,0]
GREEN  = [0,255,0]
BLUE   = [0,0,255]

# define axis for the green cross
x_axis = 800
y_axis = 600

# define size of rectangle
size_of_rectangle = 400,100

# calculate corners of rectangle based on the size of rectangle
p1 = 0,0
p2 = size_of_rectangle[0],0
p3 = size_of_rectangle[0],size_of_rectangle[1]
p4 = 0,size_of_rectangle[1]

# define rotation point (middle point) of the rectangle
rotation_point = size_of_rectangle[0]/2,size_of_rectangle[1]/2

# define offset, where to put the rectangle (in the middle) ref.point = upper left corner
rectangle_offset = 400-(size_of_rectangle[0]/2),300-(size_of_rectangle[1]/2)


# calculate new corners in the rectangle
def get_coordinates(angle,pxy,rot_point):
   v = math.pi*angle/180.0
   xn = ((pxy[0]-rot_point[0]) * math.cos(v) - (pxy[1]-rot_point[1]) * math.sin(v)) + rot_point[0]
   yn = ((pxy[0]-rot_point[0]) * math.sin(v) + (pxy[1]-rot_point[1]) * math.cos(v)) + rot_point[1]

   return xn,yn


# draw each line in the rectangle
def draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,rect_offset):
    pygame.draw.line(screen,RED,(px1+rect_offset[0],py1+rect_offset[1]),(px2+rect_offset[0],py2+rect_offset[1]),3)
    pygame.draw.line(screen,RED,(px1+rect_offset[0],py1+rect_offset[1]),(px4+rect_offset[0],py4+rect_offset[1]),3)
    pygame.draw.line(screen,RED,(px4+rect_offset[0],py4+rect_offset[1]),(px3+rect_offset[0],py3+rect_offset[1]),3)
    pygame.draw.line(screen,BLUE,(px2+rect_offset[0],py2+rect_offset[1]),(px3+rect_offset[0],py3+rect_offset[1]),3)


# rotate the rectangle
def rotate(angle):
    px1,py1 = get_coordinates(angle,p1,rotation_point)
    px2,py2 = get_coordinates(angle,p2,rotation_point)
    px3,py3 = get_coordinates(angle,p3,rotation_point)
    px4,py4 = get_coordinates(angle,p4,rotation_point)

    draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,rectangle_offset)


# draw x-/y-axis
def draw_axis():
    pygame.draw.line(screen,GREEN,(0,y_axis/2),(x_axis,y_axis/2))
    pygame.draw.line(screen,GREEN,(x_axis/2,0),(x_axis/2,y_axis))


pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False

for rotate_angle in range(0,120):
    draw_axis()
    rotate(rotate_angle)
    pygame.display.flip()
    time.sleep(0.01)
    screen.fill((0,0,0))


while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
