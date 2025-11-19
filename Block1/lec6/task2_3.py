from tkinter import *
from tkinter import messagebox

def fun1(event):
    window.geometry("560x435")
    window.config(bg="yellow")
    messagebox.showinfo("Виконано", "Зміни застосовані!")

window = Tk()
window.title("Це вікно Python")

button_1 = Button(
    window, 
    text="Змінити", 
    bg="pink", 
    fg="blue"
)
button_1.pack(expand=True)

button_1.bind("<Button-3>", fun1)
window.mainloop()