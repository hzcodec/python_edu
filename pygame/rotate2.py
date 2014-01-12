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
RED    = [255,0,0]
GREEN  = [0,255,0]
BLUE   = [0,0,255]
YELLOW = [255,255,0]

# get the coordinates for the object
def get_coord4object(obj):
    coord4object = obj.get_rect()
    return coord4object


# get the objects size in pixels
def get_object_size(obj):
    object_size = obj.get_size()
    return object_size


# get the center of the object
def get_center(obj):
    object_center = obj.get_rect().center
    return object_center


pygame.init()
screen = pygame.display.set_mode(SIZE)
done = False
screen.fill((0,0,0))

other1 = pygame.image.load("image_needle.png").convert_alpha()
other2 = pygame.transform.rotate(other1,90)
other3 = pygame.transform.rotate(other1,120)

print
print 70*'*'

# get coordinates for each object
print("Coordinates for needle 1 rectangle:",get_coord4object(other1))
print("Coordinates for needle 2 rectangle:",get_coord4object(other2))
print("Coordinates for needle 3 rectangle:",get_coord4object(other3))

# get size of each object
needle_size = get_object_size(other1)
print("Size of needle 1 rectangle:",needle_size)
offset1 = needle_size[0] / 2

needle_size = get_object_size(other2)
print("Size of needle 2 rectangle:",needle_size)
offset2 = needle_size[0] / 2

needle_size = get_object_size(other3)
print("Size of needle 3 rectangle:",needle_size)
offset3 = needle_size[0] / 2

# get center of each object
print("Center of rectangle 1:",get_center(other1))
print("Center of rectangle 2:",get_center(other2))
print("Center of rectangle 3:",get_center(other3))

# calculate pivot point
pivot_h_x1 = 214-10 
pivot_h_y1 = 225 
pivot_h_x2 = 214+10
pivot_h_y2 =  225 
pygame.draw.line(screen,BLUE,(pivot_h_x1,pivot_h_y1),(pivot_h_x2,pivot_h_y2))
pivot_v_x1 = 214 
pivot_v_y1 = 225-10 
pivot_v_x2 = 214
pivot_v_y2 =  225+10 
pygame.draw.line(screen,BLUE,(pivot_v_x1,pivot_v_y1),(pivot_v_x2,pivot_v_y2))

pivot_x = 214
pivot_y = 225


# blit all images on screen
screen.blit(other1,(COORDx,COORDy))
#screen.blit(other2,(COORDx,COORDy))
#screen.blit(other3,(COORDx,COORDy))
#screen.blit(other2,(90,212))

# draw green cross to point out pivot point of needle
pygame.draw.line(screen,GREEN,(COORDx+offset1,80),(COORDx+offset1,360))
pygame.draw.line(screen,GREEN,(70,225),(350,225))

# draw red box around object1
pygame.draw.line(screen,RED,(COORDx,COORDy),(COORDx+28,COORDy+182))
pygame.draw.line(screen,RED,(COORDx+28,COORDy),(COORDx,COORDy+182))
pygame.draw.line(screen,RED,(200,100),(228,100))
pygame.draw.line(screen,RED,(200,282),(228,282))

pygame.draw.line(screen,RED,(1,100),(30,100))
pygame.draw.line(screen,RED,(1,225),(30,225))
pygame.draw.line(screen,RED,(1,282),(30,282))

# draw blue box around object2
#pygame.draw.line(screen,BLUE,(200,100),(382,128))
#pygame.draw.line(screen,BLUE,(200,128),(382,100))
#pygame.draw.line(screen,BLUE,(200,100),(200,128))
#pygame.draw.line(screen,BLUE,(382,100),(382,128))
#pygame.draw.line(screen,BLUE,(325,1),(325,30))
#pygame.draw.line(screen,BLUE,(1,114),(30,114))

# draw yellow box around object3
#pygame.draw.line(screen,YELLOW,(200,100),(371,215))
#pygame.draw.line(screen,YELLOW,(200,215),(371,100))


pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
