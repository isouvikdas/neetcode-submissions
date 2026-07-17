# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head
        curr = prev.next
        while curr is not None:
            next_node = curr.next
            curr.next = prev

            # update
            prev = curr
            curr = next_node
        head.next = None
        return prev