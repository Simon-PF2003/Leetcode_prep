'''You are given a root and you need to return the height of a deep (longest way down). Tree has more than one children'''

class TreeNode:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children if children is not None else []

def maxDepth(root):
    if not root:
        return 0
    
    if not root.children:
        return 1
    
    heights = []
    for ch in root.children:
        heights.append(maxDepth(ch))
    return max(heights) + 1