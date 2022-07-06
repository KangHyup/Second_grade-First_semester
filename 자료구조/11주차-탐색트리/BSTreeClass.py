
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def insert_bst(t, n):
    if n.key < t.key:
        if t.left is None:
            t.left = n 
            return True
        else :
            return insert_bst(t.left, n)

    elif n.key > t.key:
        if t.right is None:
            t.right = n
            return True
        else:
            return insert_bst(t.right, n)
    else:
        return False

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=" ")
        inorder(n.right)

def delete_bst_case1(parent, node, root):
    if parent is None:
        root  = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
       child  = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    
    return root

def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while(succ.left != None):
        succp  = succ
        succ = succ.left

    if (succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right
    
    node.key = succ.key
    node.value = succ.value

    return root


def delete_bst(root, key):
    if root == None : return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else: node = node.right;

    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)
    return root