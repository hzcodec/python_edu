#   Auther      : Heinz Samuelsson
#   Date        : 2014-04-21
#   File        : class_ex1.py
#   Reference   : -
#   Description : Tkinter with class.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *
import tkMessageBox

CANVAS_WIDTH  = 600
CANVAS_HEIGHT = 200

class App(Frame):
    
    def __init__(self,parent):

        self.master = parent
        self.top = Frame(parent, width=800, height=600, borderwidth=2, relief=RAISED)
        self.top.pack_propagate(0)
        self.top.pack(side='top')

        # load images
        self.img1 = PhotoImage(file='./imgs/chicken.gif')
        self.img2 = PhotoImage(file='./imgs/chicken2.gif')

        # create canvas
        self.create_canvas()

        # create buttons
        self.create_buttons()

        
    def info(self):
        """
        Information box.
        """
        tkMessageBox.showinfo("Information box","INFO")


    def switch_bird1(self,img):
        """
        Switch to red bird.
        """
        self.canvas.create_image(50,50,image=img)
        self.canvas.create_text(180,110,font="verdena 14 bold",text="192.168.1.79")
        self.canvas.pack(padx=10,pady=10)


    def create_canvas(self):
        """
        Create a canvas within the top frame.
        """
        self.canvas = Canvas(self.top,width=CANVAS_WIDTH,height=CANVAS_HEIGHT,
                             borderwidth        = 3,
                             highlightthickness = 0,
                             background         = 'white',
                             relief             = 'raised')

        self.canvas.create_image(50,50,image=self.img1)
        self.canvas.pack(padx=10,pady=10)
 

    def create_buttons(self):
        """
        Create buttons.
        @param no input parameters
        @return no return
        """

        self.quit_button = Button(self.top, text="QUIT", fg="red", command=self.top.quit)
        self.quit_button.pack(side=LEFT)

        self.hi_button = Button(self.top, text="Hello",command=self.say_hi)
        self.hi_button.pack(side=LEFT)

        self.info_button = Button(self.top, text='Info', height=1, width=4, command=self.info)
        self.info_button.pack(side=LEFT)

        # height and width in text lines
        button1 = Button(self.top,text='Bird1',height=1, width=4,command = lambda: self.switch_bird1(self.img2))
        button1.pack(side="top", anchor=NW, padx=2, pady=2)


    def say_hi(self):
        print "Hi there"


root = Tk()
app = App(root)

root.mainloop() 

