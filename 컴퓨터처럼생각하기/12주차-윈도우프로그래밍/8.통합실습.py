from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("애완동물 선택하기")

def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    elif var.get() == 3:
        labelImage.configure(image = photo3)

labelText = Label(window, text="좋아하는 동물 투표", fg="blue", font=("궁서체", 20))

var = IntVar()
rb1 = Radiobutton(window, variable = var, value= 1, text="고양이")
rb2 = Radiobutton(window, variable = var, value= 2, text="강아지")
rb3 = Radiobutton(window, variable = var, value= 3, text="섀")
buttonOk = Button(window, text="사진보기",command=myFunc)

photo1 = PhotoImage(file= r'C:\Users\hyup98\Desktop\프로그래밍\파이썬\파이썬소스\컴퓨터처럼생각하기\12주차\cat.gif')
photo2 = PhotoImage(file= r"C:\Users\hyup98\Desktop\프로그래밍\파이썬\파이썬소스\컴퓨터처럼생각하기\12주차\dog.gif")
photo3 = PhotoImage(file= r"C:\Users\hyup98\Desktop\프로그래밍\파이썬\파이썬소스\컴퓨터처럼생각하기\12주차\bird.gif")

labelImage = Label(window, width=200, height=200, bg="yellow", image=None)

#x축과 y축에 5px정도 여유를둠
labelText.pack(padx = 5, pady= 5)
rb1.pack(padx = 5, pady= 5)
rb2.pack(padx = 5, pady= 5)
rb3.pack(padx = 5, pady= 5)
buttonOk.pack(padx = 5, pady= 5)
labelImage.pack(padx = 5, pady= 5)

window.mainloop()