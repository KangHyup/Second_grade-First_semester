#피보나치 수열출력

from circularQueue import *

Q = CircularQueue()


def getFibonacci(num1, num2, howmany):
    Q.enqueue(num1)
    Q.enqueue(num2)

    print("F(0):", num1)

    for i in range(howmany):
        nextnum = Q.dequeue() + Q.peek()
        Q.enqueue(nextnum)
        print("F(%d):"   %    int(i+1)    , Q.peek())


howmany = 9

getFibonacci(0, 1, howmany)
