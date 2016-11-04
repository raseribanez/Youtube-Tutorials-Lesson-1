# Lesson 7
# A basic GUI program

from Tkinter import *

# Create the main window for our program
top = Tk()
top.minsize(300,300) # 300 x 300 is our x and y sizes
top.title('Feet to Meters Calculator') # This is our title
top.configure(bg='DarkGrey') # This is the background color

lbl_one = Label (top, text='Enter your Value in Feet Below', fg='Blue', bg='DarkGrey', font='freesansbold, 16')
lbl_one.pack()

feet_input = Entry(top, font='freesansbold, 14', relief='raised')
feet_input.pack()

lbl_two = Label(top, text='Click Calculate to get result', fg='Blue', bg='DarkGrey', font='freesansbold, 16')
lbl_two.pack

convert_btn = Button(top, text='Calculate', fg='Blue', font='freesansbold, 14')
convert_btn.pack()

lbl_result = Label(top, relief='ridge', bg='Grey')
lbl_result.pack(fill=BOTH, expand=1)

btn_exit = Button(top, text='Exit', command=quit)
btn_exit.pack(side=BOTTOM, fill=X)

# To make Python Display the window, run a main loop:
top.mainloop()
