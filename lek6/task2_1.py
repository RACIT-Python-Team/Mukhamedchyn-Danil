from tkinter import *

def fun1(event):
    window.geometry("650x560")
    window.config(bg="green")
    button_1.config(bg="blue")

window = Tk()
window.geometry("400x300")
window.title("Вікно №1")

button_1 = Button(
    window, 
    text="Розфарбуй", 
    bg="grey", 
    fg="white"
)
button_1.place(x=100, y=90)

button_1.bind("<Button-1>", fun1)
window.mainloop()