from TreeClass import *

three= TNode(3, None, None)
one = TNode(1, None, None)
two = TNode(2, one, three)
five = TNode(5, None, None)
four = TNode(4, two, five)
eleven = TNode(11, None, None)
eight = TNode(8, None, None)
ten = TNode(10, eight, eleven)
seven = TNode(7, None, None)
nine = TNode(9, seven, ten)
root = TNode(6, four, nine)

preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)
print("\n")
levelorder(root)
