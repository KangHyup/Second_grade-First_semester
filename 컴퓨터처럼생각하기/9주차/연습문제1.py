#주관식답변 20자이상일시 통과, 아닐시 다시작성

def 사람인():
        ary = input("답변을 입력하세요: ")
        return len(ary)
        


while(True):
    howlong = 사람인()
    if  howlong > 20: print("답변은{}글자 입니다. 통과하셨습니다" .format(howlong)); break;
    else: print("답변을 다시 입력해주시요.")