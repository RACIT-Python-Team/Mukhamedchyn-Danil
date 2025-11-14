from tkinter import *
from tkinter import messagebox 

def start(event):

    user_input = entry_1.get()
    
    if user_input:
        label_1.config(text=user_input, fg="dark blue")
    else:
        
        label_1.config(text="Нічого не введено", fg="red")
        
    messagebox.showinfo(
        "Підтвердження події",
        "Дія виконана!"
    )

window = Tk()
window.title("Перше вікно")
window.geometry("600x600")
window.config(bg="orange")

entry_1 = Entry(
    window,
    width=30,
    font=("Calibri", 12)
)
entry_1.pack(pady=30)

label_1 = Label(
    window,
    text="Натисніть ПКМ по області вікна",
    fg="dark blue",
    bg="orange",
    font=("Calibri", 12)
)
label_1.pack(pady=10)

window.bind("<Button-3>", start)
window.mainloop()