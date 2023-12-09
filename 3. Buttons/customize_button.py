'''
This code will create a button containing customized text
'''

from tkinter import *

# button = you click it, then it does stuff

def click():
    print("you clicked")

window = Tk()

# Instantiating the button
button = Button (window,
                text="click me!",               #Text to display on the button
                command=click,                  #Callback function  
                font=("Comic Sans", 5),        #setting text font and size
                fg="#00FF00",                   #Setting font color
                bg="black",                     #Setting background color
                activeforeground="#00FF00",     #Setting active font color
                activebackground="black",       #Setting active background color
                state=ACTIVE)                 #Setting state
button.pack()

window.mainloop()
