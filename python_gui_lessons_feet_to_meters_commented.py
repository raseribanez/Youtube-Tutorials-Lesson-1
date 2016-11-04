#!/usr/bin/env/python
# Ben Woodfield - Python GUI - Development Lessons
# Final App - Feet to Meters Calculator - With Comments

from Tkinter import *

# Create the main window for our program
top = Tk() # Call our main window "top" for convenience later on
top.minsize(300,300) # 300 x 300 is our x and y sizes
top.title('Feet To Meters Calculator App') # This is our title
top.configure(bg='DarkGrey') # This is the background color

# These commands handle the process of taking the users input
# And putting it back to the GUI window when converted
cvt_from = StringVar()
cvt_to = StringVar()

# Here is our Function
def calculate_feet_meter():
    feet_val = float(cvt_from.get()) # The Information we take from the user (entrybox)
    meters_val = feet_val * 0.3048  # Feet to Meters Calculation
    cvt_to.set('%s Meters ' % meters_val) # The information we display back to the user (lbl_result)

# The very top label with an instruction to enter feet
lbl_info = Label(top, text='Enter your value in Feet', fg='blue', bg='DarkGrey', font='freesansbold,16') 
lbl_info.pack()

# The entry box for the users input
feet_input = Entry(top, font='freesansbold, 14', relief='raised', textvariable=cvt_from)
feet_input.pack()

# A second instruction label to press the calculate button
lbl_2 = Label(top,text='Click "Calculate" to get results', fg='blue', bg='DarkGrey', font='freesansbold,16')
lbl_2.pack()

# The main Calculate button
convert_btn = Button(top, text='Convert Feet to Meters', fg='blue', font='freesansbold, 14', command=calculate_feet_meter)
convert_btn.pack()

# The largest label - used for displaying the result in Meters
lbl_result = Label(top, textvariable=cvt_to, relief='ridge', font='freesansbold, 14', bg='Grey', fg='Blue')
lbl_result.pack(fill=BOTH, expand=1)

# The Exit button
q = Button(top, text='Exit', command=quit, bg='DarkGrey', fg='red', font='freesansbold, 14') 
q.pack(side=BOTTOM, fill=X)

# The program needs to be put into a constant loop to stay on the screen
top.mainloop()
