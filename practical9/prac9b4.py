#radiobutton

from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='male',width =25, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='female',width =25, variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='others',width =25, variable=v, value=3).pack(anchor=W)
mainloop()