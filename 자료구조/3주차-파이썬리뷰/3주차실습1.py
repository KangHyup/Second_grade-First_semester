# 수입에 따른 근로소득세 부과

income = int(input("연봉을 입력하세요 ==> "))
total = income
tax = 0
if income > 15000:
    tax += (income - 15000)*0.38    #1억5천이상- 38%
    income = 15000
if income > 8800:                   #8800~1억5천- 35%
    tax += (income - 8800)*0.35
    income = 8800
if income > 4600:
    tax += (income - 4600)*0.24
    income = 4600
if income > 1200:
    tax += (income - 1200)*0.15
    income = 1200

tax += income*0.06


print(" 전체세금 = ", tax)
print(" 순수소득 = ", total - tax)