from tkinter import *

def setup_window(event):
    window_2 = Toplevel(window)
    window_2.geometry("400x300")
    window_2.config(bg="green")
    window_2.title("Вікно №2")

window = Tk()
window.config(bg="red")
window.geometry("700x400")
window.title("Вікно №1")

window.bind("<Button-1>", setup_window)
window.mainloop()