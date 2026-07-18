# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:
        if not head:
            return False
        slow = head
        fast: Node
        if head.next:
            fast = head.next
        else:
            return False
        
        while fast.next:
            if slow == fast:
                return True
            if fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return False