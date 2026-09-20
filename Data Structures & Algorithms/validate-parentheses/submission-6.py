class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p != closeToOpen[char]:
                    return False
                
        if not stack:
            return True
        else:
            return False