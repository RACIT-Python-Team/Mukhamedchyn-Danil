from tkinter import *
from tkinter import messagebox as MessageBox

def change(event):
    user_input=int(enter1.get())
    user_input*=user_input
    MessageBox.showinfo("Ваш результат", f"Квадрат введеного числа: {user_input}")

window=Tk()
window.title("Це є вікно:)")
window.geometry("875x578")
enter1=Entry(window, width=35)
enter1.place(x=100, y=100)
window.bind("<Button-3>", change)

window.mainloop()