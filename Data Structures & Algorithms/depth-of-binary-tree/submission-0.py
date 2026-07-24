# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        q = [root, None]

        while q:
            curr_node = q.pop(0)
            if not curr_node:
                depth += 1
                if not q:
                    break
                else:
                    q.append(None)
            else:
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return depth