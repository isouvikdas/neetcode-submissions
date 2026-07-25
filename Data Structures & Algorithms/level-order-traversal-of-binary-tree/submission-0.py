# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root, None]
        level = 0
        result: list[list[int]] = [[]]
        while stack:
            curr = stack.pop(0)
            if not curr:
                if not stack:
                    break
                else:
                    stack.append(None)
                    level += 1
                    result.append([])
            else:
                print(level)
                result[level].append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return result