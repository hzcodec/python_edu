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

# initialize the library
pygame.init()

# initialize and display the window with 640x370 and name it to instrument_panel
instrument_panel = pygame.display.set_mode((640,370),0,32)

# load pictures
airspeed = pygame.image.load(img_instrument).convert_alpha()
needle   = pygame.image.load(img_needle).convert_alpha()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # put airspeed indicator on panel
    instrument_panel.blit(airspeed,(130,10))

    # draw a cross in the middle of the airspeed indicator
    pygame.draw.line(instrument_panel,(0,255,0),(310,0),(310,370))
    pygame.draw.line(instrument_panel,(0,255,0),(0,189),(640,189))

    # put the needle on the airspeed indicator
    instrument_panel.blit(needle,(287,62))
  
    # update the display
    pygame.display.flip() 
