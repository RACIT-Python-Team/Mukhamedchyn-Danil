from tkinter import *

def start(event):

    user_input = entry_1.get()
    
    if user_input: 
        label_1.config(text=user_input)
    else: 
        label_1.config(text="Ви нічого не ввели")

window = Tk()
window.config(bg="#FFCCCC") 
window.geometry("600x700")
window.resizable(False, False) 

entry_1 = Entry(
    window,
    font=("Arial", 14),
    bd=2, 
    width=30 
)
entry_1.pack(pady=20)

button_1 = Button(
    window,
    text="Ок",
    bg="white",
    font=("Calibri", 13)
)

button_1.bind("<Button-1>", start)
button_1.pack() 


label_1 = Label(
    window,
    text="Ви нічого не ввели",
    font=("Arial", 14),
    bg="#FFCCCC" 
)
label_1.pack(pady=20)

window.mainloop()