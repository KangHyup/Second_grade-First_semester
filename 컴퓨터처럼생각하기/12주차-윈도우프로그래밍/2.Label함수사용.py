from tkinter import *

window = Tk()

label1 = Label(window, text = "SWEDU~~Python을")    #window창에 text를 추가
label2 = Label(window, text = "열심히", font=("궁서체", 30), fg="blue") #폰트는 궁서체에 30, 색깔은 파랑
label3 = Label(window, text = "공부중입니다", bg="magenta",
                width=20, height=5, anchor=SE) # bg = background/ anchor = 글자위치할 장소/SE = South+East
                                               # anchor의 기본값은 CENTER며 N, NE, E, SE, S, SW, W, NW, CENTER가 있음

#pack함수를 통해 라벨을 화면에 표시
label1.pack()
label2.pack()
label3.pack()

window.mainloop()