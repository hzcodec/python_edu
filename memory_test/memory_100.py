# 
#   Auther      : Heinz Samuelsson
#   Date        : 2014-03-22
#   File        : memory_100.py
#   Reference   : -
#   Description : Generating numbers between 10-99 and its corresponding image.
#                 Images belonging to 10-19 is group 0.
#                 Images belonging to 20-29 is group 1 and so on.
#                 To run you must enter the number of groups to be displayed.
#                 Ex.
#                     > python memory_100.py 3
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame
from pygame.locals import *
import time
import random
import argparse

SCREEN_SIZE  = [800,500] # screen size
BLACK        = (0,0,0)   # background color


# group 0
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
      

# group 1
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


# group 2
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


# group 3
class Image_40():
    def __init__(self):
        self.picture = []
        self.picture.append(pygame.image.load('pic/pic40/lamp.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/jessica.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/babian.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/ren.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/tomas.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/nut.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/rubin.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/tellus.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/cock.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic40/jennie.jpg').convert())


# group 4
class Image_50():
    def __init__(self):
        self.picture = []
        self.picture.append(pygame.image.load('pic/pic50/susanne.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/banana.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/coffee.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/sabel.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/tarantulla.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/knife.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/birgitta.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/snow.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/socks.jpg').convert())
        self.picture.append(pygame.image.load('pic/pic50/milk.jpg').convert())


class Memory():

    def __init__(self,grp):
        pygame.init()
        self.surface            = pygame.display.set_mode(SCREEN_SIZE)
        self.myfont             = pygame.font.SysFont("comicsansms",55)

        self.running            = True        # running flag
        self.image_container_10 = Image_10()  # Image container
        self.image_container_20 = Image_20()  # Image container
        self.image_container_30 = Image_30()  # Image container
        self.image_container_40 = Image_40()  # Image container
        self.image_container_50 = Image_50()  # Image container
        self.img_rnd_no         = 0           # Randomly selected image
        self.x                  = 0           # x-pos for image
        self.y                  = 0           # y-pos for image
        self.group              = 0           # image group
        self.txt_label          = self.myfont.render("dummy",1,(255,0,0))
        self.ngrp               = grp

    # render image on surface, the image is scaled
    def on_render_image(self,grp,img,x,y):
        if grp == 0:
            self.surface.blit(pygame.transform.scale(self.image_container_10.picture[img-1],(160,120)),(x,y))
        elif grp == 1:
            self.surface.blit(pygame.transform.scale(self.image_container_20.picture[img-1],(160,120)),(x,y))
        elif grp == 2:
            self.surface.blit(pygame.transform.scale(self.image_container_30.picture[img-1],(160,120)),(x,y))
        elif grp == 3:
            self.surface.blit(pygame.transform.scale(self.image_container_40.picture[img-1],(160,120)),(x,y))
        elif grp == 4:
            self.surface.blit(pygame.transform.scale(self.image_container_50.picture[img-1],(160,120)),(x,y))


    # generate random number between lo and hi
    def generate_rnd_number(self,lo,hi):
        return random.randrange(lo,hi+1)


    def on_event(self,event):

        # if window closed then quit
        if event.type == QUIT:
            self.running = False

        # escape key pressed then quit
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            self.running = False

        # generate random number for selected image, x-y coordinates and group
        self.img_rnd_no = self.generate_rnd_number(1,10)
        self.x          = self.generate_rnd_number(5,650)
        self.y          = self.generate_rnd_number(5,390)
        self.group      = self.generate_rnd_number(0,self.ngrp-1)

        # calculate the offset depending of group
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

    parser = argparse.ArgumentParser()
    parser.add_argument("par1",help="memory_100.py <no_of_grps>",type=int)
    args = parser.parse_args()
    no_of_groups = args.par1

    memory_test = Memory(no_of_groups)
    memory_test.execute()


if __name__ == '__main__':
    main()
