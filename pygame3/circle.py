#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-25
#   File        : circle.py
#   Reference   : Game Programming, page 230.
#   Description : Move a circle with the mouse.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640,480))

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image,(0,0,255),(25,25),25,0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


def main():
    pygame.display.set_caption("move the circle")

    background = pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    screen.blit(background, (0,0))

    circle = Circle()
    allSprites = pygame.sprite.Group(circle)

    #pygame.mouse.set_visible(False)
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

