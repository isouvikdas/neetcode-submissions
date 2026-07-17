# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        t1, t2 = list1, list2
        dnode = Node(val = -1)
        curr = dnode
        while t1 and t2:
            if t1.val < t2.val:
                curr.next = t1
                curr = t1
                t1 = t1.next
            else:
                curr.next = t2
                curr = t2
                t2 = t2.next
        if t1:
            curr.next = t1
        else:
            curr.next = t2
        return dnode.next