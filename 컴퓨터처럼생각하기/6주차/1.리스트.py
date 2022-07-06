#리스트 선언

aa = [10, 20, 30]

#밑에 둘은 같다(밑이 더 간편)
sum = 0
for i in range(len(aa)):
    sum += aa[i]
print(sum)

sum = 0
for i in aa:
    sum += i
print(sum)

#파이썬 리스트특) 여려자료형이 들어갈 수 있음
aa = [0, "str형", 10.0, '김']


#슬라이싱: 리스트[시작:끝+1]
print(aa[2:4])
print(aa[:2])       # aa[2]까지가 아니라 그 전까지만 출력
print(aa[::])

#리스트끼리의 연산
aa=[10,20,30]
bb=[40,50,60]
print(aa + bb)      # 10,20,30,40,50,60
print(aa*3)         # 10,20,30,10,20,30,10,20,30

# 헷갈리는point
print(aa[0])        # 10이라는 str값을 출력
print(aa[0:1])      # [10]이라는 리스트를 출력. 즉 자료형이 다름

# 리스트안에 리스트
print(aa)
aa[1] = [200,201]
print(aa)

