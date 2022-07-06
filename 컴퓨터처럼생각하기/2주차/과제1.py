#2개의 숫자를 입력받고산술평균 기하평균구하기
import math
from unittest import result

a = int(input("첫번째 수: "))
b = int(input("두번째 수: "))

#산술평균
result1 = (a+b)/2 
#기하평균
result2 = math.sqrt(a*b) 
print("산술평균:", result1, "기하평균:", result2 )



