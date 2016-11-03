# Lesson 2
# A Basic GUI Program

from Tkinter import *

# Create the main window for our program
top = Tk()
top.minsize(300,300) # 300 x 300 is our x and y sizes

# Give your button a name
btn_exit = Button(top, text='Exit', command=quit)
btn_exit.pack(side=BOTTOM)

# To make Python Display the window, run a main loop:
top.mainloop()
