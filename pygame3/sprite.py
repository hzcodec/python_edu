#   Auther      : Heinz Samuelsson
#   Date        : 2014-01-25
#   File        : sprite.py
#   Reference   : Game Programming, page 230.
#   Description : Move a sprite from left to right.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx= 0 
        self.rect.centery= 200 
        self.dx = 5
        self.dy = 0

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0


def main():
    pygame.display.set_caption("basic sprite demo")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,0))
    screen.blit(background, (0,0))

    box = Box()
    allSprites = pygame.sprite.Group(box)
    
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

