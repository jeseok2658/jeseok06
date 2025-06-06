from tkinter import *

window.Tk()

window.Title("이하창놈")
window.geometry("1000x700")

label1=Label1(window,text="나는 첼시에서 행복하지 않다.",font=("궁서체",50),fg="brown",bg="blue")
photo=PhotoImage(file="루카쿠.gif")
label2=Label2(window,image=photo)

label1.pack()
label2.pack()

window.mainloop()
