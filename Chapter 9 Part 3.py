#Chapter 9 Part 3

from tkinter import *

class Ex2(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.canvas = Canvas(self, height=200, width=200)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<KeyPress>', self.mod)
        self.circle = self.canvas.create_oval(0, 0, 20, 20)
        self.canvas.focus_set()
        self.circles = []
        self.circles.append(self.circle)
        self.move()
        

    def mod (self, event):
        if event.keysym != '':
            self.circle = self.canvas.create_oval(0, 0, 20, 20)
            self.circles.append(self.circle)
    def move(self):
        for circle in self.circles:
            
            self.canvas.move(circle, 1, 1)
        self.after(100, self.move)

def runEx2():
    root = Tk()
    ex = Ex2(root)
    ex.pack()
    root.mainloop()
