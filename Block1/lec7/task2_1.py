from tkinter import *

def change(event):
    label1.config(text=enter1.get())



window=Tk()
window["bg"]="red"
window.geometry("600x700")
window.resizable(0,0)

enter1=Entry(window, font=("Arial", 14), bd=2, width=30)
enter1.place(x=150, y=200)
label1=Label(window, text="Ви нічого не ввели", font=("Arial", 14), bg="red")
label1.place(x=220, y=250)

but=Button(window, text="Ок", bg="grey", fg="white", font=("Calibri 13"))
but.place(x=300, y=150)

but.bind("<Button-1>", change)

window.mainloop()