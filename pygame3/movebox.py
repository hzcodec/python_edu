#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-22
#   File        : movebox.py
#   Reference   : Game Programming, page 144.
#   Description : Move a box from left to right.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
pygame.init()

# display
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("move a box")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,0))

box = pygame.Surface((25,25))
#box = box.convert()
# fill with red color
box.fill((255,0,0))

box_x = 0
box_y = 200

clock = pygame.time.Clock()
keepGoing = True

# loop until windows is closed
while keepGoing:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    box_x += 5

    if box_x > screen.get_width():
        box_x = 0

    screen.blit(background, (0,0))
    screen.blit(box,(box_x,box_y))
    pygame.display.flip()

