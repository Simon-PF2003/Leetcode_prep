'''Amazon's order history might be stored as a linked list, and we need to reverse the order for a specific display view.
Given the head of a singly linked list, reverse the list, and return the reversed list.'''
#input 1 -> 2 -> 3 -> 4 -> 5
#output 5 -> 4 -> 3 -> 2 -> 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def reverse_linked_list(head):
    if not head:
        return None
    if not head.next:
        [head]
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev

        prev = curr
        curr = next_node
    return prev

    