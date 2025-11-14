from tkinter import *
from tkinter import messagebox

def setup_window(event):
    window.geometry("500x600")
    window.config(bg="grey")
    window.title("8-А Клас")
    window.minsize(400, 500)
    window.maxsize(900, 1000)

def show_message(event):
    messagebox.showinfo("Повідомлення", "Я навчаюся у 8 класі!")

window = Tk()
window.bind("<KeyPress>", setup_window)
window.bind("<Button-1>", show_message)
window.mainloop()