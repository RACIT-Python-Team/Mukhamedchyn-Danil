import tkinter as tk
from Computer_vision import *



Window1 = tk.Tk()
Window1.title("Main panel")
Window1.geometry("500x500")
Window1.config(bg="#2b2b2b")

label1 = tk.Label(Window1,
                  text="Hello! \nHere you can select the different features available in this program.",
                  bg="#2b2b2b",
                  fg="white",
                  justify="left",
                  font=("Arial", 11)
                  )
label1.pack(anchor="w", padx=10, pady=10)

label2 = tk.Label(Window1,
                  text="To return to the panel, press 'q'.",
                  bg="#c0392b",
                  fg="white",
                  font=("Arial", 10, "bold")
                  )
label2.pack(anchor="w", padx=10)

but1 = tk.Button(Window1,
                 text="Hand tracking",
                 bg="#2980b9",
                 fg="white",
                 font=("Arial", 10),
                 command = hands_tracking
                 )

but1.place(x=10, y=100)
but2 = tk.Button(Window1,
                 text="Tracking object",
                 bg="#2980b9",
                 fg="white",
                 font=("Arial", 10)
                 )
but2.bind("<Button-1>", tracking_object)
but2.place(x=115, y=100)

Window1.mainloop()