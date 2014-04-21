#   Auther      : Heinz Samuelsson
#   Date        : 2014-04-21
#   File        : canvas2.py
#   Reference   : -
#   Description : Create two buttons in canvas.
#   Python ver  : 2.7.3 (gcc 4.6.3)

from Tkinter import Tk, Canvas, Frame, Button
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
 
    def print_out(self):
        print "Print out"

    def initUI(self):
        self.parent.title("Layout Test")
        self.config(bg = '#F0F0F0')
        self.pack(fill = BOTH, expand = 1)

        #create canvas
        canvas1 = Canvas(self, 
                         relief = FLAT,
                         background = "#D2D2D2",
                         width = 180, 
                         height = 500)

        canvas1.pack(side = TOP,
                     anchor = NW, 
                     padx = 10, 
                     pady = 10)

        #add quit button
        button1 = Button(canvas1,
                         text = "Quit",
                         command = self.quit,
                         anchor = W)
        button1.configure(width = 10, 
                          activebackground = "#ee0000",
                          relief = FLAT)
        button1.pack(side = TOP)

        button2 = Button(canvas1,
                         text = "Start",
                         command = self.print_out,
                         anchor = W)
        button2.configure(width = 10, 
                          activebackground = "#00ee00",
                          relief = FLAT)
        button2.pack(side = TOP)

def main():
    root = Tk()
    root.geometry('800x600+10+50')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()
