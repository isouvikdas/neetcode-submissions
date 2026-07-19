class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        longest = float('-inf')
        for i in range(len(nums)):
            ans = nums[i]
            for j in range(i+1, len(nums)):
                ans *= nums[j]
                longest = max(longest, ans, nums[j], nums[i])
        return longest