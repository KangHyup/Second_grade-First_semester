# 218p 6.4
from Nodeclass import*
from linkedList import *

ary = LinkedList()
ary.insert(0, 'A'); ary.insert(1, 'B'); ary.insert(2, 'C'); ary.insert(3, 'D');

p = ary.head
while p != None:
    print(p.data)
    p = p.link

# 6.9
def reverse(head):
    p=head
    q=None
    while p != None:
        r = q
        q = p
        p = p.link
        q.link = r
    return q

a = reverse(ary.head)

while a != None:
    print(a.data)
    a = a.link

#6.14
ary = LinkedList()
ary.insert(0, '5'); ary.insert(1, '6'); ary.insert(2, '7');
ary.append(8)
ary.display()

#6.16
ary = LinkedList()
ary.insert(0, '5'); ary.insert(1, '6'); ary.insert(2, '7');
print(ary.getSum())