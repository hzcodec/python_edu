#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-14
#   File        : box_rotate3.py
#   Reference   : www.pygame.org/wiki/RotateCenter?parent=Cookbook
#   Description : Rotate a box from 1 to 359 degress while keeping the image center.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *

RED         = (255,0,0)
GREEN       = (0,255,0)
BLACK       = (0,0,0)
SCREEN_SIZE = (640,380)

box_image   = "box2.png"
box_pos_x   = SCREEN_SIZE[0]/2
box_pos_y   = SCREEN_SIZE[1]/2
done        = False

# rotate and keep center
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

# draw a cross
def draw_cross():
    
    # draw cross in middle of box with thickness 2
    pygame.draw.line(screen,GREEN,(220,285),(460,285),2)
    pygame.draw.line(screen,GREEN,(334,160),(334,375),2)


# initialize the library
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
box    = pygame.image.load(box_image).convert_alpha()

# position the box in the middle with respect to the upper left corner
screen.blit(box,(box_pos_x,box_pos_y))

print 55*'='

box_rect = box.get_rect()

# rotate box from 1 to 360 degrees
for angle in range(1,361):

    # rotate box
    rot_image,rot_rect = rot_center(box,box_rect,angle)
    
    # new position for box
    screen.blit(rot_image,((box_pos_x+rot_rect[0]),(box_pos_y+rot_rect[1])))
    
    draw_cross()

    pygame.display.flip() 
    screen.fill((BLACK))


while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break

