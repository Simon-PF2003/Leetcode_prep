'''You are given a tree p and a tree q. You need to check if they are equal or not. Return True if they are, return False if they aren't.'''

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(p, q):
    # Usamos una sola cola que guarda PARES de nodos que deben ser iguales
    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft() # Sacamos el par actual

        # 1. Si ambos son None, este "camino" está bien, seguimos con el resto
        if not node_p and not node_q:
            continue
        
        # 2. Si uno es None o los valores son distintos, falló la comparación
        if not node_p or not node_q or node_p.val != node_q.val:
            return False
        
        # 3. Agregamos los hijos a la cola para compararlos después
        # El orden importa: comparamos Izquierda con Izquierda, y Derecha con Derecha
        queue.append((node_p.left, node_q.left))
        queue.append((node_p.right, node_q.right))

    return True