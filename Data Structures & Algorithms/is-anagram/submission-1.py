class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = [0] * 256
        for char in s:
            m[ord(char)] = m[ord(char)] + 1
        for char in t:
            m[ord(char)] = m[ord(char)] - 1
        for i in m:
            if i != 0:
                return False
        return True