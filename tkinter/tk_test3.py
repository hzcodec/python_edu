#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-30
#   File        : tk_test3.py
#   Reference   : -
#   Description : Label test with variable.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

root = Tk()

root.geometry('300x150+400+400')
var = StringVar()

lbl = Label(root,textvariable=var)
lbl.pack()

var.set('Jennie')

root.mainloop()
