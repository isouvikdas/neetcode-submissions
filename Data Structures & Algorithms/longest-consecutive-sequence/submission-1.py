class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        longest = 0
        for i in nums:
            if i not in mp:
                mp[i] = 1
        for i in nums:
            inner_longest = 0
            count = i
            while count in mp:
                inner_longest += 1
                count += 1
            longest = max(longest, inner_longest)
        return longest
