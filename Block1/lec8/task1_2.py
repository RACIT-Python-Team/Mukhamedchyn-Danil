from tkinter import *

labuba = Tk()
labuba.geometry("500x500")

canva = Canvas(labuba, width=500, height=500, bg="white")
canva.place(x=0, y=0)


canva.create_rectangle([200, 180], [400, 380], fill="#692289", width=0)


canva.create_rectangle([260, 235], [340, 300], fill="#C7C7C7", width=0)
canva.create_rectangle([205, 120], [230, 180], fill="#4bd161",width=0)
canva.create_line([260, 268], [340, 268], fill="black",width=2)
canva.create_line([300, 235], [300, 300], fill="black",width=2)

canva.create_polygon([300, 100], [170, 200], [430, 200], fill="#2667d0",width=0)



labuba.mainloop()