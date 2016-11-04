#!/usr/bin/env/python
# Ben Woodfield - Python GUI - Development Lessons
# Final App - Feet to Meters Calculator - Without Comments

from Tkinter import *

top = Tk()
top.minsize(300,300)
top.title('Feet To Meters Calculator App')
top.configure(bg='DarkGrey')

cvt_from = StringVar()
cvt_to = StringVar()

def calculate_feet_meter():
    feet_val = float(cvt_from.get())
    meters_val = feet_val * 0.3048  # Feet to Meters Calculation
    cvt_to.set('%s Meters ' % meters_val)
    
lbl_info = Label(top, text='Enter your value in Feet', fg='blue', bg='DarkGrey', font='freesansbold,16') 
lbl_info.pack()

feet_input = Entry(top, font='freesansbold, 14', relief='raised', textvariable=cvt_from)
feet_input.pack()

lbl_2 = Label(top,text='Click "Calculate" to get results', fg='blue', bg='DarkGrey', font='freesansbold,16')
lbl_2.pack()

convert_btn = Button(top, text='Convert Feet to Meters', fg='blue', font='freesansbold, 14', command=calculate_feet_meter)
convert_btn.pack()

lbl_result = Label(top, textvariable=cvt_to, relief='ridge', font='freesansbold, 14', bg='Grey', fg='Blue')
lbl_result.pack(fill=BOTH, expand=1)

q = Button(top, text='Exit', command=quit, bg='DarkGrey', fg='red', font='freesansbold, 14') 
q.pack(side=BOTTOM, fill=X)

top.mainloop()
