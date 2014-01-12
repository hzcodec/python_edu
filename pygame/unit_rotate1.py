#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-12
#   File        : unit_rotate1.py
#   Reference   : -
#   Description : Draw lines at different angles. N.B only angles between
#                 0 - 90 degrees can be handled.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import math

SIZE    = 640,480
COORDx  = 200
COORDy  = 100
RED     = [255,0,0]
GREEN   = [0,255,0]
BLUE    = [0,0,255]
YELLOW  = [255,255,0]
MAGENTA = [255,0,255]

# start values
angle  = 65   # angle 
x_pos  = 200  # x start position
y_pos  = 260  # y start position
length = 250  # length of vector


# calculate new x_pos and y_pos
def xy_pos(angle,length):
    x = math.cos(angle*math.pi/180)
    y = math.sin(angle*math.pi/180)
    return (length*x,length*y)


# draw new line corresponing to angle
def draw_line(color,x_pos,y_pos,length,new_x,new_y):
    # calculate new position for x value with offset
    t = length - round(new_x)
    pygame.draw.line(screen,color,(x_pos,y_pos),(x_pos+length-t,y_pos-round(new_y)))


pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))


# draw base line
pygame.draw.line(screen,GREEN,(x_pos,y_pos),(x_pos+length,y_pos))

# calculate new x,y pos
new_x,new_y = xy_pos(angle,length)
# draw new line
draw_line(RED,x_pos,y_pos,length,new_x,new_y)

new_x,new_y = xy_pos(68,length)
draw_line(BLUE,x_pos,y_pos,length,new_x,new_y)

new_x,new_y = xy_pos(8,length)
draw_line(YELLOW,x_pos,y_pos,length,new_x,new_y)

new_x,new_y = xy_pos(90,length)
draw_line(MAGENTA,x_pos,y_pos,length,new_x,new_y)

pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
