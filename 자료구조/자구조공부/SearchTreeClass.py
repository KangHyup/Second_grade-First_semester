from select import kevent
from tkinter import N


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def insert_bst(r, n): # r은 root노드, n은 새로 추가할노드
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

#지우려는 노드가 단일노드일때
def delete_bst_case_1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left is node:
            parent.left = None
        else:
            parent.right = None
    return root

#지우려는 노드가 자식을 하나만 가지고 있을때

def delete_bst_case_2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child
            
        return root

#지우려는 노드가 자식이 두개일때
def delete_bst_case_3(parent, node, root):
    succp = node
    succ = node.right
    while(succ.left != None):
        succp = succ
        succ = succ.left
    
    if(succp.left == succ):
        succp.left = succ.right #succ.left가 있다면 걔가 최종후보이어야 하니까 succ.left = None일수 밖에 없음
                                #따라서 후계자 부모가 연결받는건 succ.right밖에 없음
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    return root

def delete_bst(root, key):
    if root == None: return None

    parent = None
    node = root
    #탐색 시작(지울 key값을 가질 node를 찾을때까지)
    while node != None and node.key != key:
        parent = node
        if key < node.key: node = node.left #key값이 현재 노드key값보다 작으면 왼쪽으로 이동(node = root -> root.left -> root.left.left)
        else: node = node.right

    if node == None: return None #탐색실패
    #단일노드 삭제
    elif node.left == None and node.right == None:
        root = delete_bst_case_1(parent, node, root)
    #자식하나 있는 노드 삭제
    elif node.left == None or node.right == None:
        root = delete_bst_case_2(parent, node, root)
    #자식둘있는 노드 삭제
    else:
        root = delete_bst_case_3(parent, node, root)
    






