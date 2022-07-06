
outFp = None
outStr = ""

outFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일2.txt", "w" , encoding='utf - 8')

while True:
    outStr = input("내용 입력: ")
    if outStr !="":
        outFp.writelines(outStr + "\n")
    else: break

outFp.close()

print("----정상적으로 파일이 써졌음----")