import pygame
from pygame.locals import *
import time
import random

# used colors
RED         = (255,0,0)
GREEN       = (0,255,0)
BLACK       = (0,0,0)
WHITE       = (255,255,255)
# start value of counter values
START_VALUE = 20 # start value of counter values
# mouse button
LEFT        = 1
RIGHT       = 3
# screen size
SCREEN_SIZE = [920,500]


class Memory():

    def __init__(self):

        pygame.init()
        self.running     = True   # running flag
        self.image       = []     # container for all images
        self.txt_label   = []     # container for all number
        self.res_label   = "OK"   # OK/INCORRECT label
        self.rnd_number  = []     # container for all generated random numbers
        self.position    = (0,0)  # mouse position
        self.no_of_tries = 0      # number of tries  
        self.myfont     = pygame.font.SysFont("comicsansms",35)

        # coordinates for all images
        self.coordx  = [20,200,380,560,740,20,200,380,560,740]
        self.coordy  = [20,20,20,20,20,180,180,180,180,180]

        self.surface = pygame.display.set_mode(SCREEN_SIZE)

        # build up all images from 10-19
        self.image.append(pygame.image.load('pic/pic20/capsule.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/guitar.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/sugar.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/mat.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/stick.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/cactus.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/castle.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/bee.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/strawberry.jpg').convert())
        self.image.append(pygame.image.load('pic/pic20/whale.jpg').convert())

        # build up text counter values from 10-19
        for i in range(0,10):
            self.txt_label.append(self.myfont.render(str(i+START_VALUE),1,(255,0,0)))

        self.res_label = (self.myfont.render("OK",1,(255,0,0)))

        # render all images
        for i in range(0,10):
            self.on_render_image(i,self.coordx[i],self.coordy[i])

        pygame.display.flip()


    def on_event(self,event):

        self.a  = 40
        self.no = 3
        # if window closed then quit
        if event.type == QUIT:
            self.running = False

        # escape key pressed then quit
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            self.running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            # get mouse position
            self.position = pygame.mouse.get_pos()
            self.check_selection(self.position)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:

            pygame.draw.rect(self.surface,WHITE,(340,400,255,50))
            self.no_of_tries = 0
            # clear list before generating a new one
            del self.rnd_number[:]

            # generate random numbers
            for i in range(0,5):
                self.rnd_number.append(self.generate_rnd_number())
                pos = i*50
                self.on_render_number(self.rnd_number[i]-1,pos)

            pygame.display.flip()


    def get_pic_pos(self):
        if (self.position[0] > 20 and self.position[0] < 180 and self.position[1] < 140):
            return 1
        elif (self.position[0] > 200 and self.position[0] < 360 and self.position[1] < 140):
            return 2
        elif (self.position[0] > 380 and self.position[0] < 540 and self.position[1] < 140):
            return 3
        elif (self.position[0] > 560 and self.position[0] < 720 and self.position[1] < 140):
            return 4
        elif (self.position[0] > 740 and self.position[0] < 900 and self.position[1] < 140):
            return 5
        elif (self.position[0] > 20 and self.position[0] < 180 and self.position[1] > 180):
            return 6
        elif (self.position[0] > 200 and self.position[0] < 360 and self.position[1] > 180):
            return 7
        elif (self.position[0] > 380 and self.position[0] < 540 and self.position[1] > 180):
            return 8
        elif (self.position[0] > 560 and self.position[0] < 720 and self.position[1] > 180):
            return 9
        elif (self.position[0] > 740 and self.position[0] < 900 and self.position[1] > 180):
            return 10

    def check_selection(self,pos):
        print("rnd_number:",self.rnd_number)

        if (self.no_of_tries == 5):
            pygame.draw.rect(self.surface,WHITE,(340,400,255,50))
            pygame.draw.rect(self.surface,BLACK,(140,400,80,50))
            pygame.display.flip()

        else:
            pic_no = self.get_pic_pos()
            print("no_of_tries:",self.no_of_tries)
            if (pic_no == self.rnd_number[self.no_of_tries]):
                self.res_label = (self.myfont.render("OK",1,(0,255,0)))
                print("OK")
            else:
                self.res_label = (self.myfont.render("FEL",1,(255,0,0)))
                print("FEL")
    
            self.no_of_tries +=1
    
            # clear area for result label
            pygame.draw.rect(self.surface,BLACK,(140,400,80,50))
            self.surface.blit(self.res_label,(150,400))
            pygame.display.flip()

    # render image on surface
    def on_render_image(self,img,x,y):
        self.surface.blit(pygame.transform.scale(self.image[img],(160,120)),(x,y))


    # render all numbers
    def on_render_number(self,no,pos):
        self.surface.blit(self.txt_label[no],(350+pos,400))


    def on_cleanup(self):
        pygame.quit()


    # generate random number between 1-10
    def generate_rnd_number(self):
        return random.randrange(1,11)


    def execute(self):

        while(self.running):

            for event in pygame.event.get():
                self.on_event(event)
           
        self.on_cleanup()


def main():
    myMemory = Memory()
    myMemory.execute()



if __name__ == '__main__':
    main()
