#November 19, 2013 Notes

#different way
from tkinter import *

class Ex1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.bind('<KeyPress>', self.move)
        self.canvas.focus_set()

        self.circle = self.canvas.create_oval(10, 10, 40, 40)

    def move(self, event):
        if event.keysym == 'Down':
            self.canvas.move(self.circle, 0, -3)
        elif event.keysym == 'Up':
            self.canvas.move(self.circle, 0, 3)
        elif event.keysym == 'Left':
            self.canvas.move(self.circle, -3, 0)
        elif event.keysym == 'Right':
            self.canvas.move(self.circle, 3, 0)


def runEx1():
    root = Tk()
    ex = Ex1(root)
    ex.pack()
    root.mainloop()

class Circle:
    def __init__(self, canvas, radius, x, y, dx, dy):#what you need to describe a circle
        self.canvas = canvas #canvas upon which it is rendered
        self.radius = radius #how big the circle is
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.id = self.canvas.create_oval(x - radius, y-radius, x + radius, y + radius) #how to do a circle
        

class Ex2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.grid(row=0, column=0)

        self.circle = self.canvas.create_0val(10, 10, 40, 40)
        self.move()

    def move(self):
        self.canvas.move(self.circle, 3, 3)
        self.after(100, self.move)

def runEx2():
    root = Tk()
    ex = Ex2(root)
    ex.pack()
    root.mainloop()

#circle ought to have it's own class

    
