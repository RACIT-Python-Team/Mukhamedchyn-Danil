from tkinter import *
from tkinter import messagebox 

def start(event):
    
    user_input = entry_1.get()
    if (user_input.isdigit() or 
        (user_input.startswith('-') and user_input[1:].isdigit())):
        
        number = int(user_input)
        square = number * number
        
        messagebox.showinfo(
            "Результат обчислення",
            f"Добуток введеного числа на нього самого: {square}"
        )
        
    else:
        messagebox.showerror(
            "Помилка вводу",
            "Будь ласка, введіть тільки ціле число!"
        )

window = Tk()
window.title("Це є вікно :)")
window.geometry("875x578")
window.config(bg="#E0F7FA")

entry_1 = Entry(
    window,
    width=35,
    font=("Arial", 12)
)
entry_1.place(x=100, y=100)

entry_1.bind("<Button-3>", start)
window.mainloop()