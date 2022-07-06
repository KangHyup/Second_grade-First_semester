from circularQueue import *

value = CircularQueue()

for i in range(20):
    if i %3 ==0:
        value.enqueue(i)
    elif i %4 ==0:
        value.dequeue()

value.display()