from tkinter import *
from tkinter import messagebox

def fun1(event):
    window.config(bg="purple")
    button_1.config(bg="yellow")
    messagebox.showinfo("Повідомлення", "Завдання виконано!")

window = Tk()
window.geometry("500x800")
window.title("Вікно №2")

button_1 = Button(
    window, 
    text="Ок", 
    bg="lightblue", 
    fg="black"
)
button_1.place(x=200, y=390) 

button_1.bind("<Button-1>", fun1)
window.mainloop()