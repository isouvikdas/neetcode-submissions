class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        print(nums)
        result = 1
        longest = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i -1]
            if diff == 1:
                longest += 1
            elif diff == 0:
                continue
            else:
                print(i, nums[i])
                result = max(longest, result)
                longest = 1
        return max(longest, result)