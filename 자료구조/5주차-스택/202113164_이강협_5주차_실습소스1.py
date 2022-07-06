# 문자열을 거꾸로 출력하는 함수

from stackClass import Stack

instr = input("문자열 입력:")

s = Stack()
for term in instr:
    s.push(term) 

for term in instr:
    print(s.pop(),end="")
