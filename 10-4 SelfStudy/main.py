from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트","눌린 키 :"+chr(event.keycode))

def keyEvent(event):
    key = event.keysym
    is_shift = (event.state % 2) == 1


    if key in ["Up", "Down", "Left", "Right"]:
        if is_shift:
            key = "Shift+" + key
        messagebox.showinfo("키보드 이벤트", "눌린 키 : " + key)
        
window=Tk()

window.bind("<Key>",keyEvent)

window.mainloop()
