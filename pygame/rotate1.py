import pygame
from pygame.locals import *

SIZE = 640,480
pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((0,0,0))
other1 = pygame.image.load("image_needle.png").convert_alpha()
other2 = pygame.transform.rotate(other1,90)
other3 = pygame.transform.rotate(other1,180)
other4 = pygame.transform.rotate(other1,270)

needle_rect = other1.get_rect()
#(0,0 - 28,182)
print("Coordinates for needle rectangle:",needle_rect)
needle_size = other1.get_size()
print("Size of needle rectangle:",needle_size)

screen.blit(other1,(200,100))
screen.blit(other2,(90,212))
screen.blit(other3,(200,168))
screen.blit(other4,(156,210))

# draw green cross to point out pivot point of needle
pygame.draw.line(screen,(0,255,0),(214,80),(214,360))
pygame.draw.line(screen,(0,255,0),(100,225),(320,225))

# draw red diagonals to mark out the box
pygame.draw.line(screen,(255,0,0),(200,100),(228,282))
pygame.draw.line(screen,(255,0,0),(228,100),(200,282))

pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
