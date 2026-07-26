# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def inorder(node) -> TreeNode | None:
            if not node: return node

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        if len(result) >= k:
            return result[k-1]
        else:
            return -1 


    
            
            
