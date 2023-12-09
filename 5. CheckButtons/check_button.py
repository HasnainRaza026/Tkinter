'''
This code will generate a check box
'''

from tkinter import *

# checkbutton = if ticked, you agrees to something

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar() #anything stored in a variable will be an integer

check_button = Checkbutton (window,
                        text="I agree to something", #text with the checkbox
                        variable=x,                  #value of check box
                        onvalue=1,                   #value if ticked
                        offvalue=0,                  #value if not ticked
                        command=display)

check_button.pack()

window.mainloop()
