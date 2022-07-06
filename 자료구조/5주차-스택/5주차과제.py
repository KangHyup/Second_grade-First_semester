# 153p 4.12

from stackClass import Stack

s=Stack()
for i in range(10):
    if i % 3 ==0:
        s.push(i)

print(s.top)

s.clear
print(s.top)
for i in range(20):
     if i % 3 ==0:
        s.push(i)
     elif i % 4 ==0:
        s.pop()

print(s.top)