'''Try to configure the widget with various options like: bg=”red”, family=”times”,
size=18'''
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("TCSC")

C = tkinter.Canvas(window, bg="red", height=250, width=300)
C.pack()

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="olive")

# to rename the title of the window window.title("GUI")

# pack is used to show the object in the window

label = tkinter.Label(window, text="TCSC", font=("Arial Bold", 50)).pack()

window.mainloop()
