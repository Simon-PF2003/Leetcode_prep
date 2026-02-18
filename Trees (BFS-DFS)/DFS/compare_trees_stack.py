'''You are given a root and you need to return the height of a deep (longest way down). Tree has more than one children'''

class TreeNode:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children if children is not None else []
        
def isSameTree(p, q):
    # Usamos una lista como Stack
    stack = [(p, q)]

    while stack:
        # .pop() saca el ÚLTIMO que entró (el de arriba de la pila)
        node_p, node_q = stack.pop() 

        if not node_p and not node_q:
            continue
        if not node_p or not node_q or node_p.val != node_q.val:
            return False
        
        # Agregamos los hijos a la pila
        stack.append((node_p.left, node_q.left))
        stack.append((node_p.right, node_q.right))

    return True