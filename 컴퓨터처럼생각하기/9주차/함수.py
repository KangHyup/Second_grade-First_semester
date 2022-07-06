#기본양식: def 함수이름(매개변수):

def coffe_machine(botton):
    print("#1 종이컵을 내린다")
    print("#2 뜨거운물을 내린다")

    if(botton == 1): print("#3 보통커피를 내린다")
    elif(botton == 2): print("#3 설탕커피를 내린다")
    elif(botton == 3): print("#3 블랙커피를 내린다")
    else: print("#3 아무커피나 내린다")

    print("#4 커파완성!")

select = int(input("내릴 커피를 선택해 주세요) 1.보통 2.설탕 3.블랙 >>"))
coffe_machine(select)

##파이썬 함수 특
#num3이 들어오면 그 수로, 안들어오면 0으로 설정
def 더하는_함수(num1, num2, num3=0):
    return num1+num2+num3
 
# 이런식은 안됌 -> def 더하는_함수(num1=0, num2, num3):

## *매개변수: 매개변수를 튜플형태로 얼마든지 받을 수 있음
def 더하는_함수2(*num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

print(더하는_함수(1,2,3))
print(더하는_함수2(10, 50, 7, 9))

## **매개변수: 매개변수가 딕셔너리 형태로 전달
def 딕셔너리함수(**para):
    for k in para.keys():
        print("%s ---> %d 명 입니다." % (k, para[k]))   #키, 밸류값

딕셔너리함수(아이오아이 = 11 , 소녀시대 = 8, 걸스데이 = 4, AOA = 7)     #키 = 밸류