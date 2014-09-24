#November 18, 2013 Notes
#Another kind of widget
#Draws more arbritary things in a TKinter (called a canvas)


from tkinter import *
class Ex1(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<KeyPress>', self.move)

        self.circle = self.canvas.create_oval(10, 10, 30, 40)

    def move(self, event):
        print(event.keysym)
        
def runEx1():
    root = Tk()
    ex = Ex1(root)
    ex.pack()
    root.mainloop()

class Ex2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self. canvas = Canvas(self, width=300, height=300)
        self.canvas.grid(row=0, column=0)

        self.circle = self.canvas.create_oval(10, 10, 40, 40)
        self.move()

    def move(self):
        self.canvas.move(self.circle, 3,3)
        self.after(100, self.move)

def runEx2():
    root = Tk()
    ex = Ex2(root)
    ex.pack()
    root.mainloop()
    
    

        
        
