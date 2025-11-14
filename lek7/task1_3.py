from tkinter import *

def start(event):

    window.config(bg="blue")
    
    label_3 = Label(
        window,
        text="Це вікно було створено в середовищі IDLE",
        bg="blue",   
        fg="white",
        font=("Arial", 14)
    )
    label_3.place(x=200, y=250)
    
    button_1.unbind("<Button-3>")

window = Tk()
window.title("Вікно №3")
window.geometry("500x500")

button_1 = Button(window, text="Розфарбуй")
button_1.place(x=200, y=200)

button_1.bind("<Button-3>", start)
window.mainloop()