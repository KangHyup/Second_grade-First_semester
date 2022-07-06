from tkinter import *
from tkinter import messagebox

window = Tk()

def Myfuc():
    messagebox.showinfo("고양이버튼", "커여운 맹꽁이")

photo = PhotoImage(file= r'C:\Users\hyup98\Desktop\프로그래밍\파이썬\파이썬소스\컴퓨터처럼생각하기\12주차\cat.gif')
button1 = Button(window, image=photo, command=Myfuc)

button1.pack()

window.mainloop()