# 문자열의 데칼코마니 판별함수

from stackClass import Stack

instr = input("문자열 입력:") 

#대문자로 변환
instr = instr.upper()

#공백, 구두문제거
Chars = " ,.({[)}]" 
for ch in Chars:
    instr = instr.replace(ch,"")

s = Stack()
for i in range(len(instr)//2):
    s.push(instr[i])

#문자열의 길이가 짝수일때
if(len(instr)%2==0):
    for ch in instr[len(instr)//2 :]:
        Truth_Value = False
        if ch is not s.pop(): break
        Truth_Value = True

#문자열의 길이가 짝수일때
elif(len(instr)%2==1):
    for ch in instr[len(instr)//2 +1 :]:
        Truth_Value = False
        if ch is not s.pop(): break
        Truth_Value = True
    

print(Truth_Value)