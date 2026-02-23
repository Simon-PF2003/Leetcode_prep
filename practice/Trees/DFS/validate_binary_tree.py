'''At Kindle, we often need to validate the structure of our metadata to ensure searching for a specific book or chapter is lightning-fast. 
For that, we use Binary Search Trees (BST)
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Recursion
def validateBinaryTree(root):
    if not root:
        return True
    def validate(node, low = float('-inf'), high = float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

#Stack
def validateTree(root):
    if not root: 
        return True
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        node, low, high = stack.pop()
        if not (low < node.val < high):
            return False
        if node.left:
            stack.append((node.left, low, node.val))
        if node.right:
            stack.append((node.right, node.val, high))
    return True