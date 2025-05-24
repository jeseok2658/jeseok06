import random
from tkinter import *

btnList=[None]*9
fnameList=[
    "/Users/yujeseog/Downloads/짐승거인.gif",
    "/Users/yujeseog/Downloads/차력거인.gif",
    "/Users/yujeseog/Downloads/시조거인.gif",
    "/Users/yujeseog/Downloads/갑옷거인.gif",
    "/Users/yujeseog/Downloads/진격의거인.gif",
    "/Users/yujeseog/Downloads/초대형거인.gif",
    "/Users/yujeseog/Downloads/여성형거인.gif",
    "/Users/yujeseog/Downloads/턱거인.gif",
    "/Users/yujeseog/Downloads/전퇴의거인_1.gif"
]

random.shuffle(fnameList)

photoList=[None]*9
i, k = 0, 0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=PhotoImage(file=fnameList[i])
    btnList[i]=Button(window, image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()
