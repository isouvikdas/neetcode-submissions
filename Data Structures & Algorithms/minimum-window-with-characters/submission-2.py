class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("inf")
        start = 0
        freqt = [0] * 256
        freqs = [0] * 256
        for i in t:
            freqt[ord(i)] += 1

        l = 0

        for r in range(len(s)):
            freqs[ord(s[r])] += 1

            while self.contain(freqt, freqs):
                win_length = r - l + 1
                if win_length < min_len:
                    min_len = win_length
                    start = l
                print(l)
                print(s[l])
                freqs[ord(s[l])] -= 1
                l += 1

        
        if min_len == float("inf"):
            return ""
            
        return s[start: start + min_len]


    def contain(self, freqt: list[int], freqs: list[int]):
        for i in range(256):
            if freqt[i] > freqs[i]:
                return False
        return True

