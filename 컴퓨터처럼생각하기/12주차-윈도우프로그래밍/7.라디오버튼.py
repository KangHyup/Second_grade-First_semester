from tkinter import *

window = Tk()

def myFunc():
    if var.get() == 1:
        #label1의 text를 다음과 같이 바꿈
        label1.configure(text="파이썬")
    elif var.get() == 2:
        label1.configure(text="C++")
    elif var.get() == 3:
        label1.configure(text="자바")

var = IntVar()
# 누르면 변수(variable) var의 값(value)을 1로 바꾸어줌
rb1 = Radiobutton(window, text="파이썬", variable = var, value = 1, command= myFunc)
rb2 = Radiobutton(window, text="C++", variable = var, value = 2, command= myFunc)
rb3 = Radiobutton(window, text="자바", variable = var, value = 3, command= myFunc)

label1 = Label(window, text="선택한 언어 ", fg="red")

rb1.pack(); rb2.pack(); rb3.pack()
label1.pack()

window.mainloop()
