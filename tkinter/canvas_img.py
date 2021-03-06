#   Auther      : Heinz Samuelsson
#   Date        : 2014-04-21
#   File        : canvas_img.py
#   Reference   : -
#   Description : Load two gif images into a canvas.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master, 
                width  = canvas_width, 
                height = canvas_height)
canvas.pack()

img1 = PhotoImage(file = "./imgs/chicken.gif")
img2 = PhotoImage(file = "./imgs/chicken2.gif")
canvas.create_image(20,20,  anchor=NW, image=img1)
canvas.create_image(20,100, anchor=NW, image=img2)

mainloop()
