# 번호 맞추기 게임

import random
answer = random.randint(1,99)

min = 0
max = 99
trial = 0

for n in range(10) :
    guess = int(input("숫자를 입력하세요(범위:%d~%d): " % (min, max)))
    trial += 1
    if(guess > answer):
        print("아닙니다. 더 작은 숫자입니다!")
    elif(guess < answer):
        print("아닙니다. 더 큰 숫자입니다!")
    elif(guess == answer):
        print("정답입니다. %d번 만에 맞추셨습니다." % trial)
        break

print(" 게임이 끝났습니다.", sep='', end=' ')