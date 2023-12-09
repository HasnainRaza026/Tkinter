'''
This code will create a button
'''

from tkinter import *

# button = you click it, then it does stuff

def click():
    print("you clicked")

window = Tk()

# Instantiating the button
button = Button (window,
                text="click me!",               #Text to display on the button
                command=click)                  #Callback function  

button.pack()

window.mainloop()
