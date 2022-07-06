##문자열 포멧
a = "abc"
b = "123"

# 둘은 같은표현 (띄어쓰기가 다름)
print(a + b) #abc123
print(a , b) #abc 123

##방법1
#C언어처럼 사용
a = 20
print("나는 %d살 입니다" % a)   #정수형
print("나는 %s를 좋아해요" % "파이썬")  #문자열
print("Apple은 %c로 시작해요" % 'A')    #문자한개
print("나는 %s색과 숫자 %d을 좋아해요" % ("파란", 7)) #여러가지 자료형을 넣어야 할때

##방법2
#format사용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 숫자 {}을 좋아해요".format("파란", 7))
print("나는 {0}색과 숫자 {2}을 좋아해요".format("빨강","파란", 7)) #formtat안 배열의 순서대로 값을 넣어줌

##방법3
#format안에서 변수선언
print("나는{age}살이고, {color}색을 좋아해요.".format(age=20, color = "빨강"))

#밖에다 변수선언하면 에러남
age = 19
color = "노랑"
#print("나는{age}살이고, {color}색을 좋아해요.".format(age, color))     #에러

##방법4
#f를 사용하면 변수를  format안으로 가져올 수 있음
age = 19
color = "노랑"
print(f"나는{age}살이고, {color}색을 좋아해요.")