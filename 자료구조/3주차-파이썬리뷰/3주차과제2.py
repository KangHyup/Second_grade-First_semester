# 교재83p 2.2 while문을 이용한 구구단 6단 출력

i=1
while(i<10):
    print("6 * %d =" % i, 6*i)
    i+=1




# 교재84p 2.12 1+1/2+...1/n의 값을 구하는 순환함수 작성
def func (n):
    if n == 1: return 1
    else : return (1/n)+func(n-1)
    




