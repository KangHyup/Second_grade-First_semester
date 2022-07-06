from BSTreeClass import *

class BSTMap():
    def __init__(self):
        self.root = None
    
    def isEmpty(self): return self.root == None
    def clear(self): self.root == None
    def size(self): return self.count_node(self.root)
    def search(self,key): return search_bst(self.root, key)
    def count_node(self, Node):
        if Node is None:
            return 0
        else:
            return 1+self.count_node(Node.left)+self.count_node(Node.right)

    def insert(self, key, value = None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

    def delete(self, key):
        self.root = delete_bst(self.root, key)