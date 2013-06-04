#   Auther      : Heinz Samuelsson
#   Date        : 2013-06-04
#   File        : tk_canvas_test1.py
#   Reference   : -
#   Description : Tkinter with canvas test. Drawing two lines.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

root = Tk()
root.geometry('450x300+800+200')

canvas_1 = Canvas(root,width=300,height=200,background='grey')
canvas_1.grid(row=1,column=0)

lbl = Label(root,text='Coordinate')
lbl.grid(row=0,column=0)

# draw x-line, start at 10 end at 290
canvas_1.create_line(10,100,290,100)
# draw y-line, start at 10 end at 190
canvas_1.create_line(150,10,150,190)


root.mainloop()
