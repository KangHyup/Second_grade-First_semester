#사용자 입력으로부터 받은 중위표기식을 계산하여 결과 출력

from posixpath import split
from stackClass import Stack
from evalPostfix import *
from Infix2Postfix import *

instr = input("문자열 입력:")
Operator = "+-*/({[)}]"

for ch in Operator:
    instr = instr.replace(ch," "+ch+" ")

instr = instr.split()

postfix = Infix2Postfix(instr)
print(postfix)
print("계산 결과:", evalPostfix(postfix))

