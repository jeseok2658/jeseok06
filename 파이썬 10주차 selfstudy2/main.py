from tkinter import *
from tkinter import messagebox

fnameList=[
    "Kane.gif",
    "Ronaldo.gif",
    "Messi.gif",
    "Dybala.gif",
    "Mbappé.gif",
    "Lamine-Yamal.gif",
    "Salah_1.gif",
    "Dembélé.gif",
    "MartÍnez.gif"
]
num=0

def updateLabel():
    filename = fnameList[num].split("/")[-1]
    fileLabel.configure(text=filename)

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    updateLabel()  

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    updateLabel() 

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<<이전", command=clickPrev)
btnNext = Button(window, text="다음>>", command=clickNext)

photo = PhotoImage(file=fnameList[0])
pLabel = Label(window, image=photo)

fileLabel = Label(window, text=fnameList[0].split("/")[-1], font=("Arial", 14), fg="blue")

btnPrev.place(x=250, y=10)
fileLabel.place(x=350, y=15)   
btnNext.place(x=450, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
