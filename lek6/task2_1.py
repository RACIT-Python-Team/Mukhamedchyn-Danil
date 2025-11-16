from tkinter import *

def change(event):
    window1.geometry("600x400")
    window1["bg"]="green"
    but=Button(window1, text="Розфарбуй", bg="blue", fg="white")
    but.place(x=100, y=90)


window1=Tk()
window1.geometry("400x300")
window1.title("Вікно №1")
but=Button(window1, text="Розфарбуй", bg="grey", fg="white")
but.place(x=100, y=90)
window1.bind("<Button-1>", change)
window1.mainloop()