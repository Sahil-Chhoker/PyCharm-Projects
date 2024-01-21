from tkinter import *
import tkinter.messagebox

window = Tk()

window.title("TO DO List App in Python")

def enetrytask():
    input_text = ""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter Some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    entry_task=Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1,text="Add Task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


def markcompleted():
    marked = listbox_task.curselection()
    temp=marked[0]

    temp_marked = listbox_task.get(marked)

    temp_marked = temp_marked + "✔️"

    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg = "black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_tasks = Scrollbar(frame_task)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)

entry_button = Button(window, text="Add Task", width=50, command=enetrytask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
