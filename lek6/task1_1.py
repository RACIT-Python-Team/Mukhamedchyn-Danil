from tkinter import *

def setup_window(event):
    window.geometry("400x300")
    window.config(bg="green")
    window.title("Рівне") 

window = Tk()
window.bind("<Button-1>", setup_window)
window.mainloop()