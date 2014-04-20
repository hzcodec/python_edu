#   Auther      : Heinz Samuelsson
#   Date        : 2014-04-21
#   File        : radio_button1.py
#   Reference   : www.python-kurs.eu/tkinter_radiobuttons.php
#   Description : Create radio buttons.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

root = Tk()
v    = IntVar()

Label(root, 
      text    = """Choose a programming language:""",
      justify = LEFT,
      padx    = 20).pack()


Radiobutton(root,
            text     = "Python",
            padx     = 20,
            variable = v,
            value    = 1).pack(anchor=W)


Radiobutton(root,
            text     = "Perl",
            padx     = 20,
            variable = v,
            value    = 2).pack(anchor=W)

mainloop()

