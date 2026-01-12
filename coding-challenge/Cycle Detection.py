'''
Day-30
MEDIUM
Not Accepted
1/7 test cases passed
'''


# Complete the hasCycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
