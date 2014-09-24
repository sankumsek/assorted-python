#November 13, 2013 Notes
#Starting Chapter 9: Constructing GUI
#all GUI code is in module called tkinter

from tkinter import *
#main object is typically described as root
root = Tk()
def something():
    messagebox.showinfo(title="It Works!", message="Pushed")

b = Button(root, text="Push this", command=something)
b.pack() #this actually puts it in the window



#Assembling this into a regular program...

from tkinter import *
def something():
    messagebox.showinfo(title="It works!", message="Pushed")

def example1():
    root = Tk()
    b = Button(root, text="Push this", command=something)
    b.pack()
    root.mainloop()

#these components are called widgets (TK term)

#usually contain more than a single button
#create widget with everything and then create window and pack widget into it

class Square(Frame):
    def __init__(self,master):  #master is object in which is to be incorporated
        super().__init__(self,master)
        #need to use 3 kinds of widgets: text, label, and button
        label = Label(self
        
    

