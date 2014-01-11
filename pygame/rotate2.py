#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-11
#   File        : rotate2.py
#   Reference   : -
#   Description : An image of needle is rotated.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *

SIZE   = 640,480
COORDx = 200
COORDy = 100
GREEN  = [0,255,0]
RED    = [255,0,0]

pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))
other1 = pygame.image.load("image_needle.png").convert_alpha()
other2 = pygame.transform.rotate(other1,90)

needle_rect = other1.get_rect()
#(0,0 - 28,182)
print("Coordinates for needle rectangle:",needle_rect)

needle_size = other1.get_size()
print("Size of needle rectangle:",needle_size)

needle_rect_center = other1.get_rect().center
# (14,91)
print("Center of rectangle:",needle_rect_center)

screen.blit(other1,(COORDx,COORDy))
screen.blit(other2,(90,212))

# draw green cross to point out pivot point of needle
pygame.draw.line(screen,GREEN,(COORDx+14,80),(COORDx+14,360))
pygame.draw.line(screen,GREEN,(70,225),(350,225))

# draw red diagonals to mark out the box
pygame.draw.line(screen,RED,(COORDx,COORDy),(COORDx+28,COORDy+182))
pygame.draw.line(screen,RED,(COORDx+28,COORDy),(COORDx,COORDy+182))

pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
