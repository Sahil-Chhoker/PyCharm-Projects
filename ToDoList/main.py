from tkinter import *
import tkinter.messagebox

window = Tk()

window.title("TO DO List App in Python")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg = "black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scroolbar_tasks = Scrollbar(frame_task)
scroolbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scroolbar_tasks.set)
scroolbar_tasks.config(command=listbox_task.yview)




window.mainloop()
