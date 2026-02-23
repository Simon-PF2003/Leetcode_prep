'''Given the head of a linked list and two integers left and right, reverse the nodes of the list from position left to position right, and return the reversed list.'''

#Input 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
#Output = 1 -> 4 -> 3 -> 2 -> 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head, left, right):
    if not head or not left or not right or left == right:
        return None
    dummy = ListNode(0)
    dummy.next = head
    prev_to_start = dummy

    for _ in range(left - 1):
        prev_to_start = prev_to_start.next

    curr = prev_to_start.next
    for _ in range(right - left):
        curr_right = curr.next
        curr.next = curr_right.next
        curr_right.next = prev_to_start.next
        prev_to_start.next = curr_right
    return dummy.next

