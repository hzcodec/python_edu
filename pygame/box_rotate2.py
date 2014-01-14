#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-14
#   File        : box_rotate2.py
#   Reference   : -
#   Description : Rotate a box 90 degress while keeping the image center.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *

box_image = "box2.png"
RED       = (255,0,0)
GREEN     = (0,255,0)


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


# initialize the library
pygame.init()
screen = pygame.display.set_mode((640,380),0,32)
box    = pygame.image.load(box_image).convert_alpha()

screen.blit(box,(320,190))

box_rect = box.get_rect()
print "box_rec:",box_rect

rot_image,rot_rect = rot_center(box,box_rect,60)
print "rot_image:",rot_image
print "rot_rect[0]:",rot_rect[0]
print "rot_rect[1]:",rot_rect[1]

screen.blit(rot_image,((320+rot_rect[0]),(190+rot_rect[1])))

# draw cross in middle of the screen
pygame.draw.line(screen,RED,(40,190),(600,190))
pygame.draw.line(screen,RED,(320,20),(320,360))

# draw cross in middle of box
pygame.draw.line(screen,GREEN,(320,285),(348,285))
pygame.draw.line(screen,GREEN,(334,190),(334,372))

pygame.display.flip() 

while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

#  ptr_rect = ptr.get_rect()
#  print "Rectangle:",ptr_rect
#
#  img,rot_rect = rot_center(ptr,ptr_rect,45)  
#  print "rot_rect",rot_rect
#  screen.blit(img,rot_rect)
   
