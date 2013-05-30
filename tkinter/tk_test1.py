#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-30
#   File        : tk_test1.py
#   Reference   : -
#   Description : Tkinter test1.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

def button1():
    print 'Hello\n'


def button2():
    root.destroy()


root = Tk()

root.geometry('300x150+400+400')

b1 = Button(root,text='Press')
b1.grid(row=0,column=0)
b2 = Button(root,text='Quit')
b2.grid(row=0,column=1)

b1.configure(command=button1)
b2.configure(command=button2)

root.mainloop()
