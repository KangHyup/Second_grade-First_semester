from cProfile import label
from tkinter import *
from tkinter import messagebox

#이벤트가 매개변수로 들어오면 실행함
def clickLeft(event):
    messagebox.showinfo("마우스", "고양이가 왼쪽버튼으로 클릭됨")

window = Tk()
photo1 = PhotoImage(file = r"C:\Users\hyup98\Desktop\프로그래밍\파이썬\파이썬소스\컴퓨터처럼생각하기\12주차\cat.gif")
label1 = Label(window, image = photo1)

##위젯.bind("마우스 이벤트", 이벤트 함수)
#<Button-1>: 마우스 왼쪽버튼이 눌렸을때 / clickLeft를 실행해라
label1.bind("<Button-1>", clickLeft)

label1.pack(expand=10, anchor=CENTER)

window.mainloop()