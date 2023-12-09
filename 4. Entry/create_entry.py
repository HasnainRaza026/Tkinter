'''
This code will create an entry box
'''

from tkinter import *

# entry = text box that accepts single line of input

window = Tk()

# Instantiating the entry
entry = Entry(window,
              font=("Arial", 20))
entry.pack()

window.mainloop()
