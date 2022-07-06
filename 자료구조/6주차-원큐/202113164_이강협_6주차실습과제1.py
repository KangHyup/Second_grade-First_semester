#스택을 이용한 큐 구현

from stack import Stack 

S1 = Stack()
S2 = Stack()

def enqueue(val) :
    S1.push(val)

def dequeue() :
    if  S2.isEmpty():

        long = S1.size()
        for i in range(long):
            S2.push(S1.pop())

    return S2.pop()

enqueue(1)
enqueue(2)
enqueue(3)
print("dequeue() -->", dequeue())
print("dequeue() -->", dequeue())
enqueue(4);
enqueue(5);
print("dequeue() -->", dequeue())
print("dequeue() -->", dequeue())