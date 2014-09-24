#November 15, 2013 Notes
from tkinter import *

def runSquare():
    root = Tk()
    s = Square(root)
    s.pack()
    root.mainloop()

class Square2(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        label = Label(self, text="Enter x")
        label.grid(row=0, column=0)
        self.x = Entry(self)
        self.x.grid(row=0, column=1)
        self.x.bind("<KeyPress>", self.compute)
        self.result = Entry(result)
        self.result.grid(row=1, column=0, columnspan=2)

    def compute(self,event):
        if  event.keysym == "Return":   #keysym is a string that denotes what got typed (usually exactly what you typed)
            self.result.delete(0, END)
            xValue = eval(self.x.get())
            value = xValue**2
            self.result.insert(0, str(value))
            self.x.delete(0, END)
        
#Page 324 and 325 in book on how to handle different kind of events
            
