#시간과 분을 입력받아서 초로 변환

Hour = int(input("몇시간인지 입력하시오: "))
Minute = int(input("몇분인지 입력하시오: "))

Second = pow(60,2)*Hour + 60*Minute
print(Hour, "시간", Minute,"분은",Second,"초 입니다")