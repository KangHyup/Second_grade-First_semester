#두점사이의 좌표를 입력받아 두점사이의 거리를 입력받는 프로그램
# **연산자: 앞^뒤    ex) 3**2 = 9

from cmath import sqrt


X1 = int(input("첫번째 점의 X좌표를 입력하여 주십시오>>"))
Y1 = int(input("첫번째 점의 Y좌표를 입력하여 주십시오>>"))

X2 = int(input("두번째 점의 X좌표를 입력하여 주십시오>>"))
Y2 = int(input("두번째 점의 Y좌표를 입력하여 주십시오>>"))

Length = (pow(X1-X2,2)+pow(Y1-Y2,2))**0.5
print("두 점사이의 거리는", Length, "입니다")