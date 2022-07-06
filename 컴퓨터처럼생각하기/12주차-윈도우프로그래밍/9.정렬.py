from tkinter import *
from tkinter import messagebox

window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=LEFT) #side = LEFT : 왼쪽부터 채워라
button2.pack(side=LEFT)
button3.pack(side=LEFT)


# 같은걸 리스트를 이용해 구현
btnList = [None] * 3

for i in range(3):
    btnList[i] = Button(window, text="버튼" + str(i+1))

for btn in btnList:
    btn.pack(side = RIGHT, ipadx = 10) # 오른쪽부터 채워라, 버튼내부의 x크기를 조정



labelList = [None] * 3
for i in range(3):
    labelList[i] = Label(window, text="텍스트" + str(i+1))

for lab in labelList:
    lab.pack(side = TOP, pady = 10) # 위부터 채워라, y를 10만큼 띄어라

labelList = [None] * 3
for i in range(3):
    labelList[i] = Label(window, text="텍스트" + str(i+1))

for lab in labelList:
    lab.pack(side = BOTTOM) # 아래부터 채워라

window.mainloop()