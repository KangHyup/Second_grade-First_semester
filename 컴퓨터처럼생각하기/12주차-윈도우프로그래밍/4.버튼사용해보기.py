import imp
from tkinter import *

window  = Tk()

#버튼을 window에 넣음) command -> 누를시 실행될 명령어
button1 = Button(window, text="파이썬종료", fg="red", command=quit) #주의 명령어뒤 ()없어야함

button1.pack()

window.mainloop()