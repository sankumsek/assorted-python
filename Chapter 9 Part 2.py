#Chapter 9 Part 2

#9.26: Craps
from tkinter import *
import random

class Game(Frame):
    def crapsbox():
        root = Tk()
#label
        label = Label(root, text='Your roll: ')
        label.grid(row = 0, column = 0)
#entry
        rollEnt = Entry(root)
        rollEnt.grid(row=0, column=1)
#button
        button = Button(root, text='Enter', command=compute)
        button.grid(row=1, column=0, columnspan=2)

        root.mainloop()

def compute():
    
               

#9.29
   
