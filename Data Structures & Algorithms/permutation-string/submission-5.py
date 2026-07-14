class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_of_s1 = len(s1)
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord("a")
            freq1[idx] += 1
        for i in range(len(s2)):
            idx = ord(s2[i]) - ord("a")
            freq2[idx] += 1
            removable_idx = i - l_of_s1
            if removable_idx >= 0:
                freq2[ord(s2[removable_idx]) - ord("a")] -= 1
            if freq1 == freq2:
                return True
        return False