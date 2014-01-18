#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-16
#   File        : transform1.py
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
rotate_angle = 0,45,90,120

# define axis for the green cross
x_axis = 800
y_axis = 600

# define offset (in the middle)
x_offset = 300
y_offset = 250

# define offset (upper left corner)
#x_offset = 0
#y_offset = 0

# define rotation point (upper left corner)
#x_rotation_point = 0
#y_rotation_point = 0

# define rotation point (upper right corner)
x_rotation_point = 200 
y_rotation_point = 0

# define rotation point (middle point)
#x_rotation_point = 100
#y_rotation_point = 50

# define rectangle (200x100)
p1 = 0,0
p2 = 200,0
p3 = 200,100
p4 = 0,100


def get_coordinates(angle,pxy,ox,oy):

   v = math.pi*angle/180.0
   xn = ((pxy[0]-ox) * math.cos(v) - (pxy[1]-oy) * math.sin(v)) + ox
   yn = ((pxy[0]-ox) * math.sin(v) + (pxy[1]-oy) * math.cos(v)) + oy

   return xn,yn


def draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,ox,oy):
    pygame.draw.line(screen,RED,(px1+ox,py1+oy),(px2+ox,py2+oy))
    pygame.draw.line(screen,RED,(px1+ox,py1+oy),(px4+ox,py4+oy))
    pygame.draw.line(screen,RED,(px4+ox,py4+oy),(px3+ox,py3+oy))
    pygame.draw.line(screen,BLUE,(px2+ox,py2+oy),(px3+ox,py3+oy))


def draw_axis():
    pygame.draw.line(screen,GREEN,(0,y_axis/2),(x_axis,y_axis/2))
    pygame.draw.line(screen,GREEN,(x_axis/2,0),(x_axis/2,y_axis))
    pygame.draw.line(screen,YELLOW,(0,50),(200,50))
    pygame.draw.line(screen,YELLOW,(100,0),(100,100))


def print_values(a,b):
    print "xn:",a
    print "yn:",b
    print ""


pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))

for i in range(0,4):
    rotate_angle[i]
    px1,py1 = get_coordinates(rotate_angle[i],p1,x_rotation_point,y_rotation_point)
    px2,py2 = get_coordinates(rotate_angle[i],p2,x_rotation_point,y_rotation_point)
    px3,py3 = get_coordinates(rotate_angle[i],p3,x_rotation_point,y_rotation_point)
    px4,py4 = get_coordinates(rotate_angle[i],p4,x_rotation_point,y_rotation_point)
    
    draw_axis()
    draw_lines(px1,py1,px2,py2,px3,py3,px4,py4,x_offset,y_offset)

    pygame.display.flip()


while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
