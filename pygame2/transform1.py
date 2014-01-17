#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-16
#   File        : transform1.py
#   Reference   : -
#   Description : 
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import math

SIZE   = 640,480
COORDx = 200
COORDy = 100
GREEN  = [0,255,0]
RED    = [255,0,0]

# rotate angle in degrees
v = 10

# define offset
x_offset = 0
y_offset = 0

p1 = 0,0
p2 = 100,0
p3 = 100,300
p4 = 0,300


def get_coordinates(pxy,ox,oy):
   print pxy[0]
   print pxy[1]
   print "A",(pxy[0]-ox)*math.cos(v)
   print "C",(pxy[0]-ox)*math.cos(v) - (pxy[1]-oy)*math.sin(v) + ox
   xn = (pxy[0]-ox)*math.cos(v)
   print "nisse",xn

   #xn = (pxy[0]-ox)*math.cos(v) - (pxy[1]-oy)*math.sin(v) + ox
   yn = (pxy[0]-ox)*math.sin(v) + (pxy[1]-oy)*math.cos(v) + oy
   return xn,yn


def draw_line(px1,py1,px2,py2,px3,py3,px4,py4):
    pygame.draw_line(screen,RED,(px1,py1),(px2,py2))
    pygame.draw_line(screen,RED,(px1,py1),(px4,py4))
    pygame.draw_line(screen,RED,(px4,py4),(px3,py3))
    pygame.draw_line(screen,RED,(px2,py2),(px3,py3))

def print_values(a,b):
    print "xn:",a
    print "yn:",b
    print ""


pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))

pygame.draw.line(screen,GREEN,(70,225),(350,225))

px1,py1 = get_coordinates(p1,x_offset,y_offset)
print "kalle",px1,py1
print_values(px1,py1)

px2,py2 = get_coordinates(p2,x_offset,y_offset)
print "kalle",px1,py1
print_values(px1,py1)

px3,py3 = get_coordinates(p3,x_offset,y_offset)
print "kalle",px1,py1
print_values(px1,py1)

px4,py4 = get_coordinates(p4,x_offset,y_offset)
print_values(px1,py1)
pygame.display.flip()


while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
