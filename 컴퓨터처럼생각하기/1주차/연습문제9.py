#그림판 만들기
from tkinter import *
from turtle import width

##변수##
window = None
canvas = None
x1,y1,x2,y2 = None,None,None,None   #선의 시작점과 끝점

##함수##

#클릭하는 순간의 x,y좌표를 기억하는함수
def mouseClick(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

#마우스를 드랍하는 순간의 좌표를 기억하는 함수
def mouseDrop(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1,x2,y2, width = 5, fill = "red") #폭이 5인 빨간색 선을 그을것이다

##메인코드##
window = Tk()
window.title("그림판 비슷한 프로그램")
canvas = Canvas(window, height=300, width=300)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()
window.mainloop()