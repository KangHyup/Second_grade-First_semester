## 연습문제1 매출액과 매입액을 입력받아 순이익을 출력하는 프로그램

sale = int(input("수익>>"))
purchase = int(input("구매>>"))

profit = sale - purchase
print("수익 : {:0,}".format(profit))


## 연습문제2 몸무게와 신장을 입력받아 BMI를 계산해주는 프로그램
# BMI = 체중 / 키^2

weight = float(input("몸무게를 입력하시오>>"))
height = float(input("신장을 입력하시오>>"))
BMI = weight/(height**2)
print("당신의 BMI는 {:0,}입니다".format(BMI))


## 연습문제3 나눗셈을 하여 몫과 나머지를 출력하는 프로그램
num1 = float(input("숫자를 입력하시오>>"))
num2 = float(input("몇으로 나누시겠습니까?>>"))
quot = num1 // num2
remain = num1 % num2
print("몫: {:0}\n나머지:{:1}".format(quot, remain))

## 연습문제4 박테리아의 개체수 구하기
#n시간후의 박테리아수 = 초기개체수*(2^n)
start = int(input("초기 박테리아수를 입력하시오>>"))
hour = int(input("경과한 시간을 입력하시오>>"))
B_num = start*(2**hour)
print("{:0}시간후의 박테리아의 수는 {:1,}마리입니다".format(hour, B_num))

## 연습문제5 가진돈으로 연필을 몇자루사고, 거스름돈을 얼마받는지 알려주는 코드
# 연필은 개당 400원
money = int(input("지닌 금액을 입력하시오>>"))
print("{:0}로 연필{:1,}자루를 살수 있으며, 거스름돈은 {:2,}입니다".format(money, money//400, money%400))
