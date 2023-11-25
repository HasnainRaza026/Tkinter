'''
Customizing the window
'''

'''
Creating a lable
'''
#label = an area widget that holds text and/or an image within a window


from tkinter import *

window = Tk()

label = Label(window, text="Hello World") # Instantiate a lable containing text
label.pack() # Adding lable to the Window

window.mainloop()
