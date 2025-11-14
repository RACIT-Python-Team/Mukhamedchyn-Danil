from tkinter import *

def setup_window(event):
    window.geometry("700x600")
    window.config(bg="#E0B0FF")
    window.title("Назва Моєї Школи")
    window.resizable(False, False)

window = Tk()
window.bind("<Button-3>", setup_window)
window.mainloop()