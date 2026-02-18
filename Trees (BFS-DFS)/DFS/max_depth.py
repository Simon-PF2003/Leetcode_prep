'''You are given a root and you need to return the height of a deep (longest way down)'''
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return max(left_height, right_height) + 1


if __name__ == '__main__':
    # Create a sample tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = maxDepth(root)
    print(f"Max Depth: {result}")

