# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True 
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        p1 = [p]
        q1 = [q]

        while p1 or q1:
            curr_node1 = p1.pop(0)
            curr_node2 = q1.pop(0)

            if not curr_node1.left and curr_node2.left:
                return False
            if curr_node1.left and not curr_node2.left:
                return False
            if not curr_node1.right and curr_node2.right:
                return False
            if curr_node1.right and not curr_node2.right:
                return False

            if curr_node1.left and curr_node2.left:
                if curr_node1.left.val != curr_node2.left.val:
                    return False
                p1.append(curr_node1.left)
                q1.append(curr_node2.left)
            if curr_node1.right and curr_node2.right:
                if curr_node1.right.val != curr_node2.right.val:
                    return False
                p1.append(curr_node1.right)
                q1.append(curr_node2.right)
        return True        

