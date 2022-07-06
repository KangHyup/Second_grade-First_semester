#두수를 입력받고 제곱하기


#입력받기전 안내문구를 띄울수도 있음
a=int(input("제곱의 밑을 입력하세요: "))
b=int(input("지수를 입력하세요: "))
#제곱함수 pow
result = pow(a,b)
print(a, "^", b, "=", result)