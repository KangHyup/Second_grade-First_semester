# 원뿔의 부피를 계산하는 프로그램
from math import pi

radian = float(input("반지름입력 : "))
height = float(input("높이 입력 : "))
volume = pi*(radian**2)*height/3

print("원뿔의 부피 : %.1f" % volume)