from Tkinter import *
import tkMessageBox

FRAME_WIDTH   = 800
FRAME_HEIGHT  = 400
CANVAS_WIDTH  = 600
CANVAS_HEIGHT = 200


def switch_bird1(img):
    canvas.create_image(50,50,image=img)
    canvas.pack(padx=10,pady=10)

def switch_bird2(img):
    canvas.create_image(50,50,image=img)
    canvas.pack(padx=10,pady=10)

def add_bird(img):
    canvas.create_image(150,50,image=img)
    canvas.pack(padx=10,pady=10)

def hello():
    tkMessageBox.showinfo("Hello there!","Hello again")


root = Tk()

img  = PhotoImage(file='./imgs/chicken.gif')
img2 = PhotoImage(file='./imgs/chicken2.gif')

frame = Frame(width=FRAME_WIDTH,height=FRAME_HEIGHT,borderwidth=2,relief=RAISED)
frame.pack_propagate(0)
frame.pack()

canvas = Canvas(root,width=CANVAS_WIDTH,height=CANVAS_HEIGHT,
           borderwidth = 0,
           highlightthickness=0,
           background='white',
           relief = 'raised')

canvas.create_image(50,50,image=img)
canvas.pack(padx=10,pady=10)

#textBox = Label(frame,text="(x,y): ")
#textBox.pack()

# height and width in text lines
button1 = Button(frame,text='Bird1',height=1, width=4,command = lambda: switch_bird1(img2))
button1.pack(side="top", anchor=NW, padx=2, pady=2)

button2 = Button(frame,text='Bird2',command = lambda: switch_bird2(img))
button2.pack(side="top", anchor=NW, padx=2,pady=2)

button3 = Button(frame,text='Bird3',command = lambda: add_bird(img))
button3.pack(side="top", anchor=NW, padx=2,pady=2)

quit_button = Button(frame,text='Quit',height=1,width=4)
quit_button.pack(side="top", anchor=NW, padx=2,pady=2)
quit_button.bind('<Button-1>',quit)

hello_button = Button(frame,text='Hello',height=1,width=4,command = hello)
hello_button.pack(side="top", anchor=NW, padx=2,pady=2)

root.mainloop() 
