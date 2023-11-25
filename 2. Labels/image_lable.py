'''
Adding image to the Lable
'''
#label = an area widget that holds text and/or an image within a window


from tkinter import *

window = Tk()

# Converting image to photoimage format which tkinter accepts
photo = PhotoImage(file="image.png")

# Instantiate a lable containing text
label = Label(window,
            text="Hello",                   # text to display
            font=('Arial', 40, 'bold'),     # setting font
            fg='#00FF00',                   # setting font color
            bg='black',                     # setting background color
            relief=RAISED,                  # setting border
            bd=10,                          # setting border thickness
            padx=20,                        # x axis padding b/w boarder and test
            pady=20,                        # y axis padding b/w boarder and test
            image=photo,                    # providing image to the lable
            compound='bottom')              # setting location of image wrt text                       


label.pack() # Adding lable to the Window

window.mainloop()
