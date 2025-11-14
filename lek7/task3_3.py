from tkinter import *

def start(event):

    flavor = flavor_var.get()
    
    toppings = []
    if topping_choco_var.get() == 1:
        toppings.append("шоколадна присипка")
    if topping_coco_var.get() == 1:
        toppings.append("кокосова стружка")
        
    message = f"Ви обрали: {flavor} морозиво"
    
    if not toppings:
        message += " без присипки."
    elif len(toppings) == 1:
        message += f" з {toppings[0]}."
    else:
        message += f" з {toppings[0]} та {toppings[1]}."
        
    popup_window = Toplevel(window)
    popup_window.title("Ваше замовлення")
    popup_window.geometry("450x100")
    
    popup_label = Label(
        popup_window, 
        text=message, 
        font=("Arial", 12)
    )
    popup_label.pack(pady=20, padx=20)

window = Tk()
window.title("Магазин морозива 2")
window.geometry("350x300")

flavor_var = StringVar(value="ванільне")

topping_choco_var = IntVar() 
topping_coco_var = IntVar()

label_flavor = Label(window, text="Оберіть тип морозива:")
label_flavor.pack(anchor="w", padx=20)

Radiobutton(window, text="Ванільне", variable=flavor_var, value="ванільне").pack(anchor="w", padx=40)
Radiobutton(window, text="Шоколадне", variable=flavor_var, value="шоколадне").pack(anchor="w", padx=40)
Radiobutton(window, text="Фруктове", variable=flavor_var, value="фруктове").pack(anchor="w", padx=40)

label_toppings = Label(window, text="Оберіть тип присипки:")
label_toppings.pack(anchor="w", padx=20, pady=(10,0))

Checkbutton(window, text="Шоколадна присипка", variable=topping_choco_var).pack(anchor="w", padx=40)
Checkbutton(window, text="Кокосова стружка", variable=topping_coco_var).pack(anchor="w", padx=40)

button_order = Button(window, text="Замовити")
button_order.pack(pady=20)

button_order.bind("<Button-1>", start)

window.mainloop()