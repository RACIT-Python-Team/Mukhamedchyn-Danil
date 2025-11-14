from tkinter import *

def start(event):
    
    selected_flavor = flavor_var.get()
    selected_size = size_var.get()
    
    message = f"Ви вибрали {selected_flavor} морозиво у {selected_size} ріжку"
    
    popup_window = Toplevel(window)
    popup_window.title("Ваше замовлення")
    popup_window.geometry("400x100")
    
    popup_label = Label(
        popup_window, 
        text=message, 
        font=("Arial", 12)
    )
    popup_label.pack(pady=20, padx=20) 


window = Tk()
window.title("Магазин морозива")
window.geometry("350x300")

flavor_var = StringVar(value="ванільне") 
size_var = StringVar(value="маленькому")   

label_flavor = Label(window, text="Оберіть тип морозива:")
label_flavor.pack(anchor="w", padx=20)

Radiobutton(window, text="Ванільне", variable=flavor_var, value="ванільне").pack(anchor="w", padx=40)
Radiobutton(window, text="Шоколадне", variable=flavor_var, value="шоколадне").pack(anchor="w", padx=40)
Radiobutton(window, text="Фруктове", variable=flavor_var, value="фруктове").pack(anchor="w", padx=40)

label_size = Label(window, text="Оберіть розмір ріжку:")
label_size.pack(anchor="w", padx=20, pady=(10,0))

Radiobutton(window, text="Маленький", variable=size_var, value="маленькому").pack(anchor="w", padx=40)
Radiobutton(window, text="Середній", variable=size_var, value="середньому").pack(anchor="w", padx=40)
Radiobutton(window, text="Великий", variable=size_var, value="великому").pack(anchor="w", padx=40)

button_order = Button(window, text="Замовити")
button_order.pack(pady=20)

button_order.bind("<Button-1>", start)

window.mainloop()