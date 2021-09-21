# button widget
from tkinter import *
import tkinter as tk
root = Tk()
r = tk.Tk()
button = tk.Button(r, text='click me', width=25, command=r.destroy)
button.pack()
Label(root, text='Enter the College Name').grid(row=0)
Label(root, text='Enter the College Name').grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
r.mainloop()

