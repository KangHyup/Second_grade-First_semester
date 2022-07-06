# 돈을 동전으로 거슬러주는 프로그램

from cmath import pi


money, c500, c100, c50, c10 = 0,0,0,0,0

money = int(input("거슬러받을 금액을 입력하여 주십시오>>"))

c500 = money//500
money %= 500

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10
money %= 10

print("500원: %d개\n100원: %d개\n50원: %d개\n10원: %d개"% (c500,c100,c50,c10 ))
