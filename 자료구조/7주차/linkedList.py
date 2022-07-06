#링크드 리스트

from uuid import getnode
from Nodeclass import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self): 
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
            return count

    def display(self, msg='LinkedStack:'):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()
    
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else: return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem
    
    def find(self, data):
        node = self.head;
        while node is not None:
            if node.data == data : return node
            node = node.link
        return None

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    #6.14
    def append(self, elem):
        if self.head == None:
            self.head = Node(elem, self.head)
        else:
            last= self.head
            node = Node(elem, None)
            while last.link != None: 
                last = last.link

            last.link = node

    #6.16
    def getSum(self):
        sum = 0
        node = self.head
        if self.head == None: return 0
        else:
            while node != None:
                sum += int(node.data)
                node = node.link
            return sum


s = LinkedList()
s.append('A'); s.append('B'); s.append('C'); s.append('D')
s.display()
s.delete(2)
s.display()
s.delete(0)
s.display()
s.insert(1,'E')
s.display()