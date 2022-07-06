from tkinter import *

def clickMouse(event): #event = Button
    txt = ""
    #Button.num == 1: 왼쪽마우스 
    if event.num == 1:
        txt += "마우스 왼쪽버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽버튼이 ("

    #Button.x: x좌표, Button.y: y좌표
    txt += str(event.y) + ","+ str(event.x)+ ")에서 클릭됨"
    label1.configure(text = txt)

#메인코드
window = Tk()
window.geometry("400x400")

label1 = Label(window, text="이곳이 바뀜")

window.bind("<Button>", clickMouse)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()