# 117p 3.2 + 3.3 

ary =[]
ary.insert(0, 10)
ary.insert(1, 20)
ary.insert(0, 30)
ary.insert(2, 40)
ary.insert(len(ary), 50)
ary.insert(1 , 6)
ary[2] = 70
del ary[2]


print(ary)

# 3.6 리스트 내 가장큰 항목과 가장 작은항목을 반환하는 함수

ary =[3, 4, 5, 98, 1, 0]

def Find_Max_Min(ary):
    Max = Min = 0
    for num in ary:
        if num > Max: Max = num
        if num < Min: Min = num

    return Max, Min

print(Find_Max_Min(ary))
