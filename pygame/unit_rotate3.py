#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-12
#   File        : unit_rotate3.py
#   Reference   : -
#   Description : Draw lines at different angles. N.B only angles between
#                 0 - 90 degrees can be handled. Run the script with 3 parameters.
#                 The parameters are x position, y position and length of vector.
#                 Ex.
#                   > python unit_rotate3.py 250 190 125
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import math
import argparse

SIZE    = 640,480
RED     = [255,0,0]
GREEN   = [0,255,0]
BLUE    = [0,0,255]

# calculate new x_pos and y_pos
def xy_pos(angle,length):
    x = math.cos(angle*math.pi/180)
    y = math.sin(angle*math.pi/180)
    return (length*x,length*y)


# draw new line corresponding to angle
def draw_line(color,x_pos,y_pos,length,new_x,new_y):
    # calculate new position for x value with offset
    t = length - round(new_x)
    pygame.draw.line(screen,color,(x_pos,y_pos),(x_pos+length-t,y_pos-round(new_y)))

# handle in parameters
parser = argparse.ArgumentParser()
parser.add_argument("par1",type=int)
parser.add_argument("par2",type=int)
parser.add_argument("par3",type=int)
args   = parser.parse_args()
x_pos  = args.par1  # x position
y_pos  = args.par2  # y position
length = args.par3  # length of vector

pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))


# draw a red x,y line
new_x,new_y = xy_pos(0,length)
draw_line(RED,x_pos,y_pos,length,new_x,new_y)
new_x,new_y = xy_pos(90,length)
draw_line(RED,x_pos,y_pos,length,new_x,new_y)

# plot lines from angle 1-89
for angle in range(1,90):
    # calculate new x,y pos
    new_x,new_y = xy_pos(angle,length)

    if angle == 45:
        col = GREEN
    else:
        col = BLUE
    # draw new line
    draw_line(col,x_pos,y_pos,length,new_x,new_y)


pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
