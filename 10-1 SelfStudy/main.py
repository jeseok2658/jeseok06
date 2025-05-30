from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "고양이1.gif")
label1 = Label(window, image = photo1)
label1.pack(side=LEFT)

photo2 = PhotoImage(file = "고양이2.gif")
label2 = Label(window, image = photo2)
label2.pack(side=LEFT)

window.mainloop()
