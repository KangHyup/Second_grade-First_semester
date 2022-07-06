
inFp = None

inFp  = open("c:/Users/hyup98/Desktop/프로그래밍/파이썬/파이썬소스/컴퓨터처럼생각하기/10주차/HangMan.txt", "r" , encoding='utf - 8')
answer = inFp.readline()
answer = answer.lower()

shape = ['_', '_', '_', '_', '_', '_']

def search(a):
    for i in answer:
        if(a == i):
            return answer.index(i)
    return None

def CheckSucess(shape):
    if(shape.count("_") == 0): return True
    else: return False


for i in range(10):
    for j in shape:
        print(j, end="")
    print("")
    a = input("단어를 추측하세요: ")
    index = search(a)
    if(index != None): shape[index] = a
    else: print("틀렸음!")
    TryChance = 9 - i
    print("%d의 기회가 남았음!" % TryChance)
    if(CheckSucess(shape)): print("%s 사용자 승리" % answer); exit(0);

print("사용자 패배 정답은 %s" % answer)
