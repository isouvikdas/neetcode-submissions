# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:

        try:
            fast = head.next
            slow = head
            while slow and fast:
                if slow == fast:
                    return True
                slow = slow.next
                fast = fast.next.next
        except AttributeError:
            return False
        return False