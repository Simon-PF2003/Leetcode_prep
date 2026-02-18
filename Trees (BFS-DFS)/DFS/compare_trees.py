'''You are given a tree p and a tree q. You need to check if they are equal or not. Return True if they are, return False if they aren't.'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:  #If not p, q can't be empty because of the previous if and viceversa.
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


         