#   Auther      : Heinz Samuelsson
#   Date        : 2014-04-21
#   File        : radio_button2.py
#   Reference   : www.python-kurs.eu/tkinter_radiobuttons.php
#   Description : Create radio buttons.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import *

root = Tk()
v = IntVar()

# initialize choice
v.set(1)

languages = [
    ("Python",1),
    ("Perl",  2),
    ("Java",  3),
    ("C++",   4),
    ("C",     5)
]


def ShowChoice():
    print v.get()


Label(root,
      text    = """Choose a programming language:""",
      justify = LEFT,
      padx    = 20).pack()


for txt, val in languages:
    Radiobutton(root,
                text     = txt,
                padx     = 20,
                variable = v,
                command  = ShowChoice,
                value    = val).pack(anchor=W)

mainloop()

