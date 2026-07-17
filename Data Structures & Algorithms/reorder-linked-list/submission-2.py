# Definition for singly-linked list.
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reorderList(self, head: Optional[Node]) -> None:
        if not head or not head.next:
            head = head
        else:

            slow = head
            fast = head.next
            while fast.next:
                if fast.next.next:
                    slow = slow.next
                    fast = fast.next.next
                else:
                    break

            l2 = slow.next
            slow.next = None
            # Reverse the right half of the list
            # l2 is the head for the right half list
            prev = l2
            curr = l2.next
            while curr:
                next_node = curr.next
                curr.next = prev

                # update
                prev = curr
                curr = next_node
            l2.next = None

            # l1 is the head for left half list and l2 is the reversed head for the right half list
            l1 = head
            l2 = prev
            dnode = Node(-1)
            curr = dnode

            # merge two lists l1 & l2
            while l1 and l2:
                curr.next = l1
                curr = l1
                l1 = l1.next
                curr.next = l2
                curr = l2
                l2 = l2.next

            head = dnode.next



