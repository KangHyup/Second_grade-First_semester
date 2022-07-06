#로또 번호 출력하기

import random

def getNumber():
    return random.randrange(1,46)

lotto = []
num = 0

while(True):
    num = getNumber()

    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >=6: break

print("로또번호>>", end="")
lotto.sort()
for i in lotto:
    print(i, end=" ")