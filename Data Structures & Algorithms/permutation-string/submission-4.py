class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l_of_s1 = len(s1)
        substring = []
        for i in range(len(s2)):
            substring.append(s2[i])
            if len(substring) > l_of_s1 - 1:
                if len(substring) > l_of_s1:
                    substring.pop(0)
                if sorted(substring) == s1:
                    return True
        return False