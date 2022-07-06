#숫자를 입력받아 숫자만큼의 변의 길이를 가진 별모양 출력
# *turtle을 사용해서*
import turtle

turtle.shape('turtle')
Length = int(input("한변의 길이를 입력하시오>>"))

#반복문
for i in range(5):
    turtle.forward(Length)
    turtle.right(144)


turtle.done()
