'''
This code will create an entry c=box with the buttons
'''

from tkinter import *

# entry = text box that accepts single line of input

def submit():
    username = entry.get() # gets the text entered into the entry box
    print("Hello "+username)

def delete():
    entry.delete(0,END) # removes all the text written to the entry box

def backspace():
    entry.delete(len(entry.get())-1,END) # removes the last letter of text written to the entry box

window = Tk()

# Instantiating the entry
entry = Entry(window,
              font=("Arial", 20))

entry.pack(side=LEFT) # Entry box will be on left side

submit_button = Button(window, text="submit", command=submit) 
submit_button.pack (side=RIGHT) # Submit button will be on right side

delete_button = Button(window, text="delete", command=delete) 
delete_button.pack (side=RIGHT) # Delete button will be on right side

back_button = Button(window, text="backspace", command=backspace) 
back_button.pack (side=RIGHT) # Backspace button will be on right side

#entry.insert(0. 'Spongebob')  ---> adds default text in the entry box
#entry.config(show="*")       ---> hides the text in the entry box  
# #entry.config(state=DISABLED)    ---> disable the entry box

window.mainloop()
