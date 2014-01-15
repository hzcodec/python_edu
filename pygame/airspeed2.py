#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-10
#   File        : airspeed1.py
#   Reference   : -
#   Description : An image of an airspeed and a needle is showed in a window.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *

# image names used locally
img_instrument = "image_airspeed.png"
img_needle     = "image_needle.png"

needle_angle = 89 # degrees
done         = False

# rotate and keep center
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


# initialize the library
pygame.init()

# initialize and display the window with 640x370 and name it to instrument_panel
instrument_panel = pygame.display.set_mode((640,370),0,32)

# load pictures
airspeed = pygame.image.load(img_instrument).convert_alpha()
needle   = pygame.image.load(img_needle).convert_alpha()

for needle_angle in range(0,360):    
    # put airspeed indicator on panel
    instrument_panel.blit(airspeed,(130,10))

    # draw a cross in the middle of the airspeed indicator
    pygame.draw.line(instrument_panel,(0,255,0),(310,0),(310,370))
    pygame.draw.line(instrument_panel,(0,255,0),(0,189),(640,189))

    box_rect = needle.get_rect()
    rot_image,rot_rect = rot_center(needle,box_rect,needle_angle)
    instrument_panel.blit(rot_image,((267+rot_rect[0]),(83+rot_rect[1])))

    # update the display
    pygame.display.flip() 

while not done:
   for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break

