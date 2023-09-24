import tkinter
from tkinter import *
from PIL import ImageTk


def call():
    window.destroy()
    import nextPage

window = Tk()
window.geometry('400x896')
window.resizable(False, False)
window.title('todo list')
bgImage = ImageTk.PhotoImage(file='1.png')
bgLabel = Label(window, image=bgImage)
bgLabel.place(x=0, y=0)
startButton = Button(window, text="START", font=("Segoe UI Semibold", 25, "bold"), fg="#3B93AA",
                     bg="#e8e6d9", cursor='hand2', borderwidth=0, activeforeground='#e8e6d9', activebackground="#e8e6d9"
                     , command=call)
startButton.place(x=144, y=425)


window.mainloop()
