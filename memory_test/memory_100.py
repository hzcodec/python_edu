import pygame
from pygame.locals import *
import time
import random

# screen size
SCREEN_SIZE  = [800,500]
# background color
BLACK = (0,0,0)

START_VALUE = 10


class Image_10():
    def __init__(self):
        self.picture = []
        self.picture.append(pygame.image.load('pic/pic10/emil.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/fish.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/wave.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/lucia.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/hat.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/baby.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/pistol.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/lipstick.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/tiger.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic10/table.jpg').convert())
      

class Image_20():
    def __init__(self):
        self.picture = []
        self.picture.append(pygame.image.load('pic/pic20/capsule.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/guitar.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/sugar.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/mat.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/stick.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/cactus.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/castle.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/bee.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/strawberry.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic20/whale.jpg').convert())


class Image_30():
    def __init__(self):
        self.picture = []
        self.picture.append(pygame.image.load('pic/pic30/hook.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/nubbe.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/sack.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/water.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/baker.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/vase.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/dinosaur.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/pizza.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/sandal.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic30/squirell.jpg').convert())


class Memory():

    def __init__(self):
        pygame.init()
        self.surface            = pygame.display.set_mode(SCREEN_SIZE)
        self.myfont             = pygame.font.SysFont("comicsansms",55)

        self.running            = True        # running flag
        self.image_container_10 = Image_10()  # Image container
        self.image_container_20 = Image_20()  # Image container
        self.image_container_30 = Image_30()  # Image container
        self.img_rnd_no         = 0           # Randomly selected image
        self.x                  = 0           # x-pos for image
        self.y                  = 0           # y-pos for image
        self.group              = 0           # image group
        self.txt_label          = self.myfont.render("dummy",1,(255,0,0))

    # render image on surface, the image is scaled
    def on_render_image(self,grp,img,x,y):
        if grp == 0:
            self.surface.blit(pygame.transform.scale(self.image_container_10.picture[img-1],(160,120)),(x,y))
        elif grp == 1:
            self.surface.blit(pygame.transform.scale(self.image_container_20.picture[img-1],(160,120)),(x,y))
        elif grp == 2:
            self.surface.blit(pygame.transform.scale(self.image_container_30.picture[img-1],(160,120)),(x,y))


    # generate random number between 1-10
    def generate_rnd_number(self,lo,hi):
        return random.randrange(lo,hi+1)


    def on_event(self,event):

        # if window closed then quit
        if event.type == QUIT:
            self.running = False

        # escape key pressed then quit
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            self.running = False

        # generate random number for various objects
        self.img_rnd_no = self.generate_rnd_number(1,10)
        self.x          = self.generate_rnd_number(5,650)
        self.y          = self.generate_rnd_number(5,390)
        self.group      = self.generate_rnd_number(0,2)

        # calculate the offset for each group
        offset = self.group*10 + 10

        # render the text
        self.txt_label = self.myfont.render(str((self.img_rnd_no-1)+offset),1,(255,0,0))
        self.surface.blit(self.txt_label,(self.x,self.y))
        pygame.display.flip()
        time.sleep(3)

        # render the image
        self.on_render_image(self.group,self.img_rnd_no,self.x,self.y)
        pygame.display.flip()
        time.sleep(1)
        self.surface.fill(BLACK)
        

    def execute(self):
        while(self.running):

            for event in pygame.event.get():
                self.on_event(event)
           

def main():
    memory_test = Memory()
    memory_test.execute()


if __name__ == '__main__':
    main()
