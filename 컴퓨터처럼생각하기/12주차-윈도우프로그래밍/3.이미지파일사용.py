from tkinter import *

window = Tk()

#gif만 잘불러오고 다른건 다른 코드 필요
photo = PhotoImage(file = 'cat.gif')
label1  = Label(window, image = photo)

label1.pack()

window.mainloop()
 