from tkinter import *
from tkinter import messagebox

def FtoC(F):
    return (F-32)/1.8

def FtoK(F):
    return (F-32)/1.8 + 273.15

def change():
    try:
        degree = float(input_F.get())
    except:
        messagebox.showinfo("", "화씨에 실수만 입력하세요")
    else:
        input_C.insert(0, str(FtoC(degree)))
        input_K.insert(0, str(FtoK(degree)))


window = Tk()
window.geometry("250x100")

label_F = Label(window, text="화씨 ", width=10)
label_C = Label(window, text="섭씨 ")
label_K = Label(window, text="절대온도 ")
label_F.grid(row=0, column=0)
label_C.grid(row=1, column=0)
label_K.grid(row=2, column=0)

input_C = Entry(window, width=20)
input_F = Entry(window, width=20)
input_K = Entry(window, width=20)
input_F.grid(row=0, column=1)
input_C.grid(row=1, column=1)
input_K.grid(row=2, column=1)


button1 = Button(window, text="온도 변환", command= change)
button1.grid(row=3, column=1)

window.mainloop()
