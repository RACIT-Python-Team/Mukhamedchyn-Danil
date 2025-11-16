from tkinter import *

def newtext(event):
    if color_var.get() == 1 and paint_var.get() == 2:
        label["text"] = "Ви вибрали жовту гуаш"
        Window["bg"] = "yellow"

    elif color_var.get() == 2 and paint_var.get() == 1:
        label["text"] = "Ви вибрали зелену акварель"
        Window["bg"] = "green"

    elif color_var.get() == 1 and paint_var.get() == 1:
        label["text"] = "Ви вибрали жовту акварель"
        Window["bg"] = "yellow"

    elif color_var.get() == 2 and paint_var.get() == 2:
        label["text"] = "Ви вибрали зелену гуаш"
        Window["bg"] = "green"

Window = Tk()
Window.geometry("400x400")
label = Label(Window, text="Не вибрано")
label.place(x=100, y=50)
color_var = IntVar(value=1)
paint_var = IntVar(value=1)
Radiobutton(Window, text="Жовтий", variable=color_var, value=1).place(x=100, y=100)
Radiobutton(Window, text="Зелений", variable=color_var, value=2).place(x=100, y=120)
Radiobutton(Window, text="Акварель", variable=paint_var, value=1).place(x=100, y=160)
Radiobutton(Window, text="Гуаш", variable=paint_var, value=2).place(x=100, y=180)

label.bind("<Button-1>", newtext)
Window.mainloop()