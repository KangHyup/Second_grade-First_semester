from TreeClass import *

def swapNodes(p) :
        if p:
            p.left, p.right = swapNodes(p.right), swapNodes(p.left)
            return p
        return None

def reverse(root) :
    print(" 트리의 좌우를 교환합니다.")
    swapNodes(root)

f = TNode('F', None, None)
e = TNode('E', f, None)
d = TNode('D', None, None)
c = TNode('C', None, None)
b = TNode('B', d, c)
root = TNode('A', e, b)

print('\n Level-Order: ', end="")
levelorder(root)

reverse(root)

print('\n Level-Order: ', end="")
levelorder(root)