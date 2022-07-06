# 홀수와 짝수를 구분하는 프로그램

num = int(input("수입력 : "))

if(num%2==0):
    print("짝수 입니다.")
elif(num%2==1):
    print("홀수 입니다.")
elif(num==0):
    print("0 입니다.")
else:
    print("홀수도 짝수도 아닙니다.")