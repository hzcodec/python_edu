#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-30
#   File        : tk_test2.py
#   Reference   : -
#   Description : Create a window with a label.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

root = Tk()

root.geometry('300x150+400+400')

lbl = Label(root,text='Hello')
lbl.pack()

root.mainloop()
