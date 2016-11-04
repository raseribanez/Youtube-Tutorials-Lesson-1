# Lesson 9
# A basic GUI program

from Tkinter import *

# Create the main window for our program
top = Tk()
top.minsize(300,300) # 300 x 300 is our x and y sizes
top.title('Feet to Meters Calculator') # This is our title
top.configure(bg='DarkGrey') # This is the background color

# These commands handle the process of taking the users input
# And putting it back to the GUI eindoe when converted
cvt_from = StringVar()
cvt_to = StringVar()

# Here is our function
def calculate_feet_meter():
    feet_val = float(cvt_from.get()) # What we pull from the entrybox for calculating
    meters_val = feet_val * 0.3048 # Our main calculation / conversion from feet to meters
    cvt_to.set('%s Meters ' % meters_val) # What we display back to the GUI

lbl_one = Label (top, text='Enter your Value in Feet Below', fg='Blue', bg='DarkGrey', font='freesansbold, 16')
lbl_one.pack()

feet_input = Entry(top, font='freesansbold, 14', relief='raised', textvariable=cvt_from)
feet_input.pack()

lbl_two = Label(top, text='Click Calculate to get result', fg='Blue', bg='DarkGrey', font='freesansbold, 16')
lbl_two.pack

convert_btn = Button(top, text='Calculate', fg='Blue', font='freesansbold, 14', command=calculate_feet_meter)
convert_btn.pack()

lbl_result = Label(top, relief='ridge', bg='Grey', font='freesansbold, 16', fg='Blue', textvariable=cvt_to)
lbl_result.pack(fill=BOTH, expand=1)

btn_exit = Button(top, text='Exit', command=quit)
btn_exit.pack(side=BOTTOM, fill=X)

# To make Python Display the window, run a main loop:
top.mainloop()
