class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float("inf")
        start = 0
        freq_t = [0] * 256
        freq_s = [0] * 256
        for char in t:
            freq_t[ord(char)] += 1
        l = 0

        for r in range(len(s)):
            freq_s[ord(s[r])] += 1

            while self.contain(freq_t, freq_s):
                window_length = r - l + 1
                if window_length < min_length:
                    min_length = window_length
                    start = l
                freq_s[ord(s[l])] -= 1
                l += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]


    def contain(self, freq_t: list[int], freq_s: list[int]) -> bool:
        for i in range(256):
            if freq_t[i] > freq_s[i]:
                return False
        return True
