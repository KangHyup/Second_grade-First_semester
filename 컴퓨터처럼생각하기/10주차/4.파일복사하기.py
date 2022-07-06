inFp = None
inStr = ""

outFp = None
outStr = ""


inFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일.txt", "r" , encoding='utf - 8')
outFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일2.txt", "w" , encoding='utf - 8')


inList = inFp.readlines()

for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("----정상적으로 파일이 복사됌----")