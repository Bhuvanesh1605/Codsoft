import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def add_task():
    todo = TaskEntry.get()
    if todo != " ":
        task_list.insert(tkinter.END, todo)
        TaskEntry.delete(0, tkinter.END)
    elif todo == " ":
        messagebox.showwarning('ERROR', 'Enter the task')


def delete_action():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning('Error', 'Select the task to delete')

def popup():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
        messagebox.showinfo('Message', 'Congratulation')
    else:
        messagebox.showinfo('Error', 'Select the Finshed task')



window = Tk()
window.geometry('400x896')
window.title("todo List")
window.resizable(True,True)
bgImage1 = ImageTk.PhotoImage(file='2.png')
bgLabel = Label(window, image=bgImage1)
bgLabel.place(x=0, y=0)
TaskEntry = Entry(width=40, font=('Trajan Pro', 13), bd=0, fg='black', bg='#F4EEEE', )
TaskEntry.place(x=10, y=175)
AddButton = Button(window, text="Add Task", font=("Copperplate Gothic", 12, "bold"), fg="black",
                   bg="#e8e6d9", cursor='hand2', bd=0, activeforeground='#e8e6d9', activebackground="#e8e6d9", width=8,
                   command=add_task)
AddButton.place(x=150, y=220)
task_list = Listbox(window, font=("Copperplate Gothic", 15, "bold"), fg="black",
                    bg="#F4EEEE", cursor='hand2', bd=0, width=46, height=10, selectmode= tkinter.SINGLE)
task_list.place(x=0, y=260)
scoller = tkinter.Scrollbar(window)
scoller.pack(side=tkinter.RIGHT, fill=BOTH)
DeleteButton_Task = Button(task_list, text="Delete ", font=("Copperplate Gothic", 12, "bold"), fg="#451952",
                           bg="#F0F0F0", cursor='hand2', bd=0, activeforeground='#071952', activebackground="#451952",
                           width=8, command=delete_action)
DeleteButton_Task.place(x=110, y=190)
FinshButton_Task = Button(task_list, text="Finish ", font=("Copperplate Gothic", 12, "bold"), fg="#451952",
                          bg="#F0F0F0", cursor='hand2', bd=0, activeforeground='#071952', activebackground="#451952",
                          width=8, command=popup)
FinshButton_Task.place(x=200, y=190)
window.mainloop()
