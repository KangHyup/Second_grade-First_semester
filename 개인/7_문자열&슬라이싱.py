## 문자열
# 큰따옴표 작은따옴표 상관없음
sentence = '나는 소년입니다' 
print(sentence)

sentence2 = "파이썬은 쉬워요잉"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요"""
print(sentence3)

##슬라이싱
# 문자열의 [N]번째 정보를 가져옴
jumin = "981213-1234567"

print("성별: "+ jumin[7])
print("출생연도: "+ jumin[0:2]) # 0번째 부터 (2-1)번째 까지
print("출생월: "+ jumin[2:4])
print("출생일: "+ jumin[4:6])

print("생년월일: "+ jumin[:6]) # 시작이 공석이면 자동으로 처음부터
print("주민뒷자리: "+ jumin[7:]) # 끝이 공석이면 자동으로 끝까지
print("주민뒷자리(뒤에서부터): "+ jumin[-7:]) # 맨 뒤 7번째부터 끝까지 ex) jumin[-1] == 7