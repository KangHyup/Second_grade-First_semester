# 개발연도를 출력하는 프로그램

Dict1 = { "C":1972, "java": 1995, "python":1991, "go":2009, "pascal": 1969}


while(True):
    whatlang = input("프로그래밍 언어 입력: ")
    result = False

    for i in Dict1.keys():
        if whatlang == i:
            print("%s는 %d년에 태어났어요" % (i, Dict1.get(i)))
            result = True
    if result == False:
        print("알 수 없는 정보입니다.")