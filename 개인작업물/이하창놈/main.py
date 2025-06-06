from tkinter import *

window.Tk()

window.Title("이하창놈")
window.geometry("1000x700")

label1=Label1(window,text="나는 첼시에서 행복하지 않다.",font=("궁서체",50),fg="brown",bg="blue")
photo=PhotoImage(file="uGR-naglw3v_dJadrPT-tjZNWnJk291j9YM8HRY9Gy2-KOu4d0lN6D-8eNd59Q4UvTXBTWERaWj0PlBab20cg1r11OXt7QPs89X6.gif")
label2=Label2(window,image=photo)

label1.pack()
label2.pack()

window.mainloop()
