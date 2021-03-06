#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-16
#   File        : transform2.py
#   Reference   : -
#   Description : Rotate a rectangle around different points.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import math

SIZE   = 800,600
COORDx = 200
COORDy = 100
RED    = [255,0,0]
GREEN  = [0,255,0]
BLUE   = [0,0,255]
YELLOW = [255,255,0]

# rotate angle in degrees
rotate_angle = 45

# define axis for the green cross
x_axis = 800
y_axis = 600

# define offset, where to put the rectangle (in the middle)
rectangle_offset = 300,250

# define rotation point (middle point)
rotation_point = 100,50

# define rectangle (200x100)
p1 = 0,0
p2 = 200,0
p3 = 200,100
p4 = 0,100


def get_coordinates(angle,pxy,rot_point):
   v = math.pi*angle/180.0
   xn = ((pxy[0]-rot_point[0]) * math.cos(v) - (pxy[1]-rot_point[1]) * math.sin(v)) + rot_point[0]
   yn = ((pxy[0]-rot_point[0]) * math.sin(v) + (pxy[1]-rot_point[1]) * math.cos(v)) + rot_point[1]

   return xn,yn


def draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,rect_offset):
    pygame.draw.line(screen,RED,(px1+rect_offset[0],py1+rect_offset[1]),(px2+rect_offset[0],py2+rect_offset[1]))
    pygame.draw.line(screen,RED,(px1+rect_offset[0],py1+rect_offset[1]),(px4+rect_offset[0],py4+rect_offset[1]))
    pygame.draw.line(screen,RED,(px4+rect_offset[0],py4+rect_offset[1]),(px3+rect_offset[0],py3+rect_offset[1]))
    pygame.draw.line(screen,BLUE,(px2+rect_offset[0],py2+rect_offset[1]),(px3+rect_offset[0],py3+rect_offset[1]))


def rotate(angle):
    px1,py1 = get_coordinates(angle,p1,rotation_point)
    px2,py2 = get_coordinates(angle,p2,rotation_point)
    px3,py3 = get_coordinates(angle,p3,rotation_point)
    px4,py4 = get_coordinates(angle,p4,rotation_point)

    draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,rectangle_offset)


def draw_axis():
    pygame.draw.line(screen,GREEN,(0,y_axis/2),(x_axis,y_axis/2))
    pygame.draw.line(screen,GREEN,(x_axis/2,0),(x_axis/2,y_axis))


def print_values(a,b):
    print "xn:",a
    print "yn:",b
    print ""


pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))

rotate(rotate_angle)
rotate(165)

draw_axis()

pygame.display.flip()


while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
