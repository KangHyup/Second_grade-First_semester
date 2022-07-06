from email import message
from tkinter import *
from tkinter import messagebox

def whatkey(event): #event = Key
    ##Key.keycode : 눌린키를 반환
    #showinfo("알림창 제목", "내용")
    messagebox.showinfo("키보드 이벤트", "눌린키 : "+chr(event.keycode))

window = Tk()

window.bind("<Key>", whatkey)
window.mainloop()