#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-30
#   File        : tk_test4.py
#   Reference   : -
#   Description : Changing variable.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

def button1():

    v = var.get()
    if v == 'Jennie':
        var.set('Mattias')
    else:
        var.set('Jennie')


def button2():
    root.destroy()


root = Tk()

root.geometry('300x150+400+400')
var = StringVar()
var.set('Jennie')

lbl = Label(root,textvariable=var)
lbl.pack()

b1 = Button(root,text='Press')
b2 = Button(root,text='Quit')

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b1.configure(command=button1)
b2.configure(command=button2)

lbl.grid(row=1,column=0)

root.mainloop()
