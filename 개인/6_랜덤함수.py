# 랜덤함수
from random import *

print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(random()*10) # 0.0~10.0 미만의 임의의 값 생성 **위보다 크다는 보장이 없음**

print(int(random()*10)) # 0~10미만의 임의의 정수값 생성
print(int(random()*10) + 1) # 1~10이하의 임의의 정수값 생성

print(int(random()*45) + 1) # 1~45이하의 임의의 정수값 생성

print(int(randrange(1, 46))) # 1~46*미만*의 임의의 정수값 생성
print(randint(1, 46)) # 1~45*이하*의 임의의 정수값 생성