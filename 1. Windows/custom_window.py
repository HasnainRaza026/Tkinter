'''
Customizing the window
'''

# Import everything related to tkinter
from tkinter import *

window = Tk() #instantiate an instance of a window

window.geometry("420x420") # Sets the size of the window

window.title("My First Window") # Sets the title of the window

icon = PhotoImage (file='image.png') # Converts image to Photoimage format, which tkinter accepts
window.iconphoto (True, icon) # Sets window icon

# config() function used to make changes to the window
window.config(background='black') # Chnage the background color, takes color name or HEX value

window.mainloop() #place window on computer screen listen for events
