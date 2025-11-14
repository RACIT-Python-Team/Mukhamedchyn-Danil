import tkinter as tk


window = tk.Tk()
window.title("Вікно №1")
window.geometry("500x500")


label_1 = tk.Label(
    window,
    text="Це вікно було створено в середовищі IDLE",
    bg="blue",         
    fg="white",         
    font=("Arial", 14)  
)
label_1.pack(pady=50) 
window.mainloop()