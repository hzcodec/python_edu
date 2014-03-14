# reference : http://pygametutorials.wikidot.com/tutorials-two

import pygame
from pygame.locals import *
import time
import random

RED         = (255,0,0)
GREEN       = (0,255,0)
BLACK       = (0,0,0)
IMAGE_DELAY = 2
LEFT        = 1
RIGHT       = 3


class Memory():

    def __init__(self):
        pygame.init()
        self.running = True


    def on_init(self):
        self.display_surf = pygame.display.set_mode((800,600))
        self.myfont       = pygame.font.SysFont("comicsansms",35)
        self.pos          = (0,0)                                  # mouse position
        self.image        = []
        self.txt_label    = []
        self.a            = 80
        self.b            = 0
        self.no           = 2
 
        # build up all images from 10-19
        self.image.append(pygame.image.load('pic/pic30/hook.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/nubbe.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/sack.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/water.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/baker.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/vase.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/dinosaur.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/pizza.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/sandal.jpg').convert())
        self.image.append(pygame.image.load('pic/pic30/squirell.jpg').convert())

        # build up text counter values from 30 - 39
        for i in range(0,10):
            self.txt_label.append(self.myfont.render(str(i+30),1,(255,0,0)))

        # generate first image and the number list on surface
        self.on_render_image(2,80,80)
        self.on_render_numbers()
        pygame.display.flip()


    def on_render_selection(self,sel,res,col):
        label = self.myfont.render(sel,1,(255,255,0))
        self.display_surf.blit(label,(200,45))
        label2 = self.myfont.render(res,1,col)
        self.display_surf.blit(label2,(200,85))


    def check_answer(self,no,pos):
        selection = -1 

        # check mouse y-position 
        if (pos[1] < 20 or pos[1] < 50):
            s_selection =  "Krok"
            selection = 0
        elif (pos[1] < 80 or pos[1] < 104):
            s_selection = "Nubbe"
            selection = 1
        elif (pos[1] < 130 or pos[1] < 152):
            s_selection = "Sack"
            selection = 2
        elif (pos[1] < 170 or pos[1] < 201):
            s_selection = "Vatten"
            selection = 3
        elif (pos[1] < 230 or pos[1] < 251):
            s_selection = "Bagare"
            selection = 4
        elif (pos[1] < 277 or pos[1] < 297):
            s_selection = "Vas"
            selection = 5
        elif (pos[1] < 330 or pos[1] < 352):
            s_selection = "Dinosaurie"
            selection = 6
        elif (pos[1] < 380 or pos[1] < 399):
            s_selection = "Pizza"
            selection = 7
        elif (pos[1] < 430 or pos[1] < 450):
            s_selection = "Sandal"
            selection = 8
        elif (pos[1] < 480 or pos[1] < 505):
            s_selection = "Ekorre"
            selection = 9
        else:
            s_selection = "Inget vald"
            selection = -1 

        # check result of selection
        if (no == selection):
            s_result = "Korrekt val!"
            col = GREEN
        else:
            s_result = "Ej korrekt val!"
            col = RED

        self.on_render_selection(s_selection,s_result,col)


    def on_event(self,event):
        if event.type == QUIT:
            self.running = False
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:

            # get mouse position, generate number for image and check answer
            self.no  = self.generate_rnd_number()
            self.on_render_image(self.no,self.a,self.a)

            # swap coordinates so image is moving every time
            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            self.pos = pygame.mouse.get_pos()
            self.check_answer(self.no,self.pos)
            self.on_render_image(self.no,self.a,self.a)
            pygame.display.flip()


    # render randomly selected image on surface
    def on_render_image(self,img,x,y):
        self.display_surf.blit(pygame.transform.scale(self.image[img],(160,120)),(150+x,150+y))


    # render all numbers
    def on_render_numbers(self):
        for i in range(0,10):
            self.display_surf.blit(self.txt_label[i],(500,i*50+15))


    def on_cleanup(self):
        pygame.quit()


    def generate_rnd_number(self):
        return random.randrange(0,10)


    def on_execute(self):

        if self.on_init() == False:
            self.running = False
         
        while(self.running):

            self.on_render_numbers()

            # get mouse position then render images
            for event in pygame.event.get():
                self.on_event(event)
           
            self.display_surf.fill(BLACK)

        self.on_cleanup()


def main():
    myMemory = Memory()
    myMemory.on_execute()



if __name__ == '__main__':
    main()
