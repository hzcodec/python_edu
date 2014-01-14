#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-14
#   File        : box_rotate2.py
#   Reference   : www.pygame.org/wiki/RotateCenter?parent=Cookbook
#   Description : Rotate a box 90 degress while keeping the image center.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *

RED         = (255,0,0)
GREEN       = (0,255,0)
SCREEN_SIZE = (640,380)

box_image   = "box2.png"
box_pos_x   = SCREEN_SIZE[0]/2
box_pos_y   = SCREEN_SIZE[1]/2

# rotate and keep center
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


# initialize the library
pygame.init()
#screen = pygame.display.set_mode((640,380),0,32)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
box    = pygame.image.load(box_image).convert_alpha()

# position the box in the middle with respect to the upper left corner
screen.blit(box,(box_pos_x,box_pos_y))

print 55*'='

box_rect = box.get_rect()
print "box_rec:",box_rect

# rotate 60 degrees
rot_image,rot_rect = rot_center(box,box_rect,60)
print "rot_image:",rot_image
print "rot_rect[0]:",rot_rect[0]
print "rot_rect[1]:",rot_rect[1]

# new position for box
screen.blit(rot_image,((box_pos_x+rot_rect[0]),(box_pos_y+rot_rect[1])))

# draw cross in middle of the screen with thickness 2
pygame.draw.line(screen,RED,(40,190),(600,190),2)
pygame.draw.line(screen,RED,(320,20),(320,360),2)

# draw cross in middle of box with thickness 2
pygame.draw.line(screen,GREEN,(320,285),(348,285),2)
pygame.draw.line(screen,GREEN,(334,190),(334,372),2)

pygame.display.flip() 


while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
