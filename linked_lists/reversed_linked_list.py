'''Given the head of a linked list, reverse it and return the new head.'''
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
    
    def reverseList(head):
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        return prev