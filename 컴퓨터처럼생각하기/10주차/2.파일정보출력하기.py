import os

inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명을 입력하시오>> ")

#os함수를 이용하여 파일이없어도 에러가 안나오도록
if os.path.exists(fName):
    inFp = open(fName, "r", encoding='utf-8')

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end='')

    inFp.close()
else:
    print("파일이 없습니다")


