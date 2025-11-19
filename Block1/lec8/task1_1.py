from tkinter import *

labuba = Tk()
labuba.geometry("500x500")

canva = Canvas(labuba, width=500, height=500, bg="white")
canva.place(x=0, y=0)

canva.create_rectangle([120, 100], [280, 460], fill="#7C7C7C", width=0)

canva.create_polygon([200, 30], [80, 100], [320, 100], fill="#606060",width=0)
canva.create_oval([150,340],[250,440],fill="#970303",width=0 )
canva.create_oval([150,120],[250,220],fill="#229d1b",width=0 )
canva.create_oval([150,230],[250,330],fill="#eaff00",width=0 )


labuba.mainloop()