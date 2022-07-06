
from linkedList import LinkedList

class Term :
    def __init__( self, expon, coeff ):
        self.expon = expon #정수(차수)
        self.coeff = coeff #소수(계수)


class SparsePoly(LinkedList):
    def __init__( self ):
        super().__init__()

    # 최고차항의 계수를 리턴하는 함수
    def degree(self) :
        node  = self.head
        Max_expon  = 0
        while not node == None:
            if(node.data.expon > Max_expon): Max_expon = node.data.expon
            node = node.link
        return Max_expon

    def display(self, msg=""):
        print("\t", msg, end='')
        node = self.head
        while not node == None:
            print("  ", node.data.coeff, "  x^", node.data.expon,"  +" , end=' ')
            node = node.link
        print()
    
     # 차수와 계수를 입력받고 짤라서 term에계수와 지수를 넣어버림
    def read(self):
        self.clear()
        pos = 0
        while True :
            token = input("계수 차수 입력(종료:-1): ").split(" ")
            if token[0] == '-1' :
                self.display("입력 다항식:")
                return 0
            else:  
                self.insert(pos, Term(int(token[1]), float(token[0])))
                pos += 1
          
    def add(self, B):
        C = SparsePoly()
        a = self.head
        b = B.head
        pos = 0 
        while a!=None or b!=None :
            if a==None or (b!=None and a.data.expon < b.data.expon) :
                C.insert(pos, Term(b.data.expon, b.data.coeff))
                pos +=1
                b = b.link
            elif b==None or (a!=None and a.data.expon > b.data.expon) :
                C.insert(pos, Term(a.data.expon, a.data.coeff))
                pos +=1
                a = a.link
            else :
                C.insert(pos, Term(a.data.expon , a.data.coeff + b.data.coeff ))
                pos+=1
                a = a.link; b = b.link
                
        return C


A = SparsePoly()
A.read()

B = SparsePoly()
B.read()

A.display("A = ")
B.display("B = ")

C = A.add(B)
C.display("A+B = ")
