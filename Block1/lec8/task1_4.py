from tkinter import *

labuba = Tk()
labuba.geometry("500x500")

canva = Canvas(labuba, width=500, height=500, bg="white")
canva.place(x=0, y=0)
canva.create_oval([9,140],[300,445],fill="#8a2f2f",width=0 )
canva.create_oval([40,180],[290,440],fill="#0f1054",width=0 )
canva.create_oval([55,205],[280,440],fill="#8a2f2f",width=0 )
canva.create_oval([65,232],[270,438],fill="#0f1054",width=0 )
canva.create_oval([85,260],[260,438],fill="#8a2f2f",width=0 )
canva.create_oval([115,290],[255,430],fill="#0f1054",width=0 )
canva.create_oval([130,310],[246,428],fill="#8a2f2f",width=0 )
canva.create_oval([160,350],[230,420],fill="#0f1054",width=0 )
labuba.mainloop()