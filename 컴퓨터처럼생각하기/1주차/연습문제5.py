#닭, 돼지, 소의 총 다리 수 구하기

Chicken = int(input("닭의 마릿수를 입력하시오: "))
Pig = int(input("돼지의 마릿수를 입력하시오: "))
Cow = int(input("소의 마릿수를 입력하시오: "))

SumLeg = 2*Chicken + 4*Pig + 4*Cow
print("총 다리의 갯수는", SumLeg, "입니다")