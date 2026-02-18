'''A linked list is failing and its last node, instead of pointing to None, points to one of the previous nodes, creating an infinite. Return True if there's
a cycle and False if there isn't'''

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def linked_list_cycle(head):
        if not head or not head.next:
            return False
        
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False