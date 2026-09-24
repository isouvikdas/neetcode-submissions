class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        result = 1
        longest = 1

        for i in range(len(nums)):
            if i == 0:
                continue
            diff = nums[i] - nums[i-1]
            if diff == 1:
                longest += 1
                result = max(longest, result)
            elif diff == 0:
                continue
            else:
                longest = 1

        return result