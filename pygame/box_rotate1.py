#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-14
#   File        : box_rotate1.py
#   Reference   : -
#   Description : Rotate a box 90 degress while keeping the image center.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *

box_image = "box2.png"
RED       = (255,0,0)
GREEN     = (0,255,0)

# initialize the library
pygame.init()
screen = pygame.display.set_mode((640,380),0,32)
box    = pygame.image.load(box_image).convert_alpha()

screen.blit(box,(320,190))

rotated_box = pygame.transform.rotate(box,90)
screen.blit(rotated_box,(320,190))

pygame.draw.line(screen,RED,(40,190),(600,190))
pygame.draw.line(screen,RED,(320,20),(320,360))

pygame.display.flip() 

while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

