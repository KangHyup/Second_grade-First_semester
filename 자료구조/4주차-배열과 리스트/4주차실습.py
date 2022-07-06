from audioop import reverse

class Polynomial :
    def __init__( self ):
        self.ary = []
    def degree(self) :
        return len(self.ary)-1
    def display(self, msg="f(x) = "):
        print(msg, end="")
        for i in range (len(self.ary)):
            num = int(len(self.ary)-1-i)         #num은 차수를 의미
            if i == len(self.ary)-1:             # 상수항은 숫자만 출력
                print(self.ary[num])
            
            else:                               # 그외는 차수와 +기호출력
                print(self.ary[num], "x^%d + " %num, end="")
    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree() :     #a배열이 더 길때
            p.ary = list(self.ary)
            for i in range (len(b.ary)):
                p.ary[i] += b.ary[i]

        else :                              #b배열이 더 길때
            p.ary = list(b.ary)
            for i in range (len(self.ary)):
                p.ary[i] += self.ary[i]
        return p

    def eval(self, x):
        Sum =0
        for i in range(len(self.ary)):
            Sum += self.ary[i]*(x**i)
        return Sum
        
    def read(self): # split / reverse 메소드 함수 활용
        self.ary = list(map(float, input("최고차항부터 계수를 순서대로 입력하시오: ").split()))
        self.ary.reverse()

a = Polynomial()
b = Polynomial()
a.read()
b.read()
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("A+B = ")
print("B(2) = ", b.eval(2))