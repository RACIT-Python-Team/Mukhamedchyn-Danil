from tkinter import *

labuba = Tk()
labuba.geometry("500x500")

canva = Canvas(labuba, width=500, height=500, bg="white")
canva.place(x=0, y=0)
canva.create_oval([9,140],[300,440],fill="#fde800",width=2, outline="#fd3b00")
canva.create_polygon([160, 380], [65, 350], [250, 350], fill="#DD9F42",width=2, outline="#66460f")
canva.create_rectangle([152, 285], [168, 325], fill="#38387f",width=0)
canva.create_oval([190,270],[240,220],fill="#c5c5c5",width=2 )
canva.create_oval([215,265],[235,245],fill="#000000",width=2 )
canva.create_oval([70,270],[120,220],fill="#c5c5c5",width=2 )
canva.create_oval([95,265],[115,245],fill="#000000",width=2 )

labuba.mainloop()