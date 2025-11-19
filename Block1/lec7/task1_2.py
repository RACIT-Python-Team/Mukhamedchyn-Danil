from tkinter import *

def start(event):

    label_2 = Label(
        window,
        text="Функція виконана",
        bg="green",
        fg="white",
        font=("Calibri", 14)
    )
    label_2.pack(pady=50)
    
    window.unbind("<KeyPress>")

window = Tk()
window.title("Вікно №2")
window.geometry("500x500")

window.bind("<KeyPress>", start)

window.mainloop()