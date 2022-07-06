#

while True:
    qus = input("\n질문입력 >>")

    #1
    if qus.find("안녕") >=0 :
        print("안녕하세요, 만나서 반가워요")
    #2
    elif qus.find("파이썬") >=0 :
        print("파이썬 재밌지요. 열심히 공부하세요.")
    #3
    elif qus.find("음악") >=0 :
        print("저는 힙합음악을 좋아해요")
    #4
    elif qus.find("가수") >=0 :
        print("저는 창모라는 가수를 제일 좋아해요")
    #5
    elif qus.find("가족") >=0 :
        print("저는 부모님과 남동생한명이 있답니다")
    #6
    elif qus.find("고향") >=0 :
        print("제 고향은 인천이에요")
    #7
    elif qus.find("취미") >=0 :
        print("저는 음악을 듣는걸 좋아해요")
    #8
    elif qus.find("날씨") >=0 :
        print("오늘은 전반적으로 화창할 예정이에요")
    #9
    elif qus.find("알람") >=0 :
        print("오후 6시에 알람이 설정되어있어요")
    #9
    elif qus.find("미세먼지") >=0 :
        print("오늘의 미세먼지는 맑음, 초미세먼지도 맑음입니다")

    else:
        print("질문을 이해하지 못했습니다")