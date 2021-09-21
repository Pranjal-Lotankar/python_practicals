#checkbutton widget
from tkinter import *
root = Tk()
v1 = IntVar()
Checkbutton(root, text='Python',width =25, variable=v1).grid(row=0, sticky=S)
v2 = IntVar()
Checkbutton(root, text='Unix',width =25, variable=v2).grid(row=1, sticky=S)
v3 = IntVar()
Checkbutton(root, text='Perl',width =25, variable=v3).grid(row=2, sticky=S)
mainloop()

