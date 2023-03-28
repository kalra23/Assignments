#Determine whether a tree is a valid binary search tree
#A binary search tree is a tree with two children, left and right and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if node.val < min_val or node.val > max_val:
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

#Passing values in code to check it is binary search tree or not

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


if is_bst(root):
    print("The binary tree is a valid binary search tree")
else:
    print("The binary tree is not a valid binary search tree")
