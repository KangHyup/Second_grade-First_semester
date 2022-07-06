#ord()함수: 문자의 고유한 숫자를 알려줌
print("파 ->", ord("파"))

#chr()함수: 숫자의 해당하는 문자를 알려줌
print("54028 ->", chr(54028))


#암호화 함수 만들기
inFp, outFp = None, None
inStr, outStr = "", ""
i =0
secu = 0

secuYN = input("1.암호화 2.암호화해석 >>")

if secuYN == "1":
    secu = 100
elif secuYN == "2":
    secu = -100

#함수메커니즘) 암호화:
inFp = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일.txt", 'r', encoding='utf-8')
outFp  = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/텍스트파일2.txt", 'w', encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr: break;

    outStr = ""
    for i in range(len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr+ch2

        outFp.write(outStr)

outFp.close()
inFp.close()
print('변환완료')