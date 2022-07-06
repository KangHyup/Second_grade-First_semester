
'''## open 함수
변수 = open("파일명", "r") #읽기용, 뒤에 r없어도 기본으로 이거

변수 = open("파일명", "r+") #읽기 + 쓰기

변수 = open("파일명", "w") #쓰기용, 기존에 파일이 있으면 덮어씀

변수 = open("파일명", "a") #쓰기용, 기존에 파일이 있으면 이어서씀'''

inFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일.txt", "r", encoding="utf-8")

##텍스트파일을 출력하는 여러가지 방법
# 1. while문
print("readline()함수 + while 사용")
while True:
    #readline() 파일을 한줄씩 읽음
    inStr = inFp.readline()
    if inStr == "": break; # 다음라인이 없는경우 탈출

    print(inStr, end='')    #이래도 붙여서 출력 안됌
print("\n")

inFp = None
inList = ""
inFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일.txt", "r", encoding="utf-8")

# 2. readlines()로 한번에 불러오기
inList = inFp.readlines() #텍스트파일을 줄마다 *리스트화*해서 저장
print("readlines()함수 사용")
for i in inList:
    print(i, end='')

inFp = None
inList = ""
inFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일.txt", "r", encoding="utf-8")

inFp.close()