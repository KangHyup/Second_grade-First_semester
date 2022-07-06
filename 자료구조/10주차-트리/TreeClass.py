from circularQueue import CircularQueue

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def count_node(Node):
    if Node is None:
        return 0
    else:
        return 1+count_node(Node.left)+count_node(Node.right)

def calc_height( Node):
    if Node is None:
        return 0
    hLeft = calc_height(Node.left)
    hRight = calc_height(Node.right)
    if(hLeft > hRight):
        return hLeft+1
    else:
        return hRight+1

def preorder( Node):
    if Node is not None:
        print(Node.data, end =" ")
        preorder(Node.left)
        preorder(Node.right)

def inorder( Node):
    if Node is not None:
        inorder(Node.left)
        print(Node.data, end=" ")
        inorder(Node.right)

def postorder( Node):
    if Node is not None:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.data, end=" ")

def count_leaf( Node):
    if Node is None:
        return 0
    elif Node.left is None and Node.right is None:
        return 1
    else:
        return count_leaf(Node.left) + count_leaf(Node.right)

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=" ")
            queue.enqueue(n.left)
            queue.enqueue(n.right)
