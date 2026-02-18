'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#Recursion
def compareChildren(left_child, right_child):
    if left_child is None and right_child is None:
        return True
    if left_child is None or right_child is None:
        return False
    if left_child.val == right_child.val:
        return compareChildren(left_child.left, right_child.right) and compareChildren(left_child.right, right_child.left)
    else:
        return False

def simmetricTree(root):
    if not root:
        return True
    
    return compareChildren(root.left, root.right)

#Stack

def simmetricTree(root):
    if not root:
        return True

    stack = [(root.left, root.right)]

    while stack:
        left_children, right_children = stack.pop()

        if not left_children and not right_children:
            continue

        if not left_children or not right_children or left_children.val != right_children.val:
            return False
        
        stack.append((left_children.left, right_children.right))
        stack.append((left_children.right, right_children.left))

    return True


