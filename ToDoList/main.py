from tkinter import *
import tkinter.messagebox

window = Tk()

window.title("TO DO List App in Python")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg = "black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)






window.mainloop()
