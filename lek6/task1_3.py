from tkinter import *

def setup_window(event):
    window.geometry("300x200")
    window.config(bg="yellow")
    window.title("Ім'я Прізвище")
    window.minsize(200, 100)
    window.maxsize(1000, 900)

window = Tk()
window.bind("<KeyPress>", setup_window)
window.mainloop()