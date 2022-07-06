lyrics = """
하늘에서는 호우주의보 호우주의
준비됐어 난 호우주의보 호우주의
바다를 끌어 올려 비를 내려, 호우주의
숨도 못 쉴 테니 호흡 주의
아무리 찔려도 일어나 무한의 주인
옛날에 쑥덕대던 애들 이제 무안하지
걍 내 삶을 표현하지, 아니 걍 초월하지
처음 만난 사이 악수하듯 꿈은 손 내밀지
Yo 언제까지 소년일지"""

while True:
    print("\n", lyrics)
    print("-"*30)
    orgword = input("수정될 단어 입력: ")
    chword = input("수정할 단어 입력: ")
    lyrics = lyrics.replace(orgword, chword)
    print("-"*30)
