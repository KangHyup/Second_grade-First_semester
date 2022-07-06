#함수 type: 변수의 종류를 알려줌

myVar = 10 #정수형 int
print(type(myVar))

myVar = 10.0 #실수형 float
print(type(myVar))

myVar = "10" #문자열 str
print(type(myVar))

myVar = True #참거짓 bool
print(type(myVar))

#밑의 둘은 같은 표현
var1=var2=var3=300
var3=100    #var3부터 변수가 들어감
var2=var3
var1=var2

var1 = var2 + 10.0
print(var1)     #110.0(실수형)

