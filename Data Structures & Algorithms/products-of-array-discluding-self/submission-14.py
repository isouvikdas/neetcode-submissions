class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            res = 1 if i == 0 else result[i - 1] * nums[i - 1]
            result.append(res)
        
        suffix = [1] * len(nums)
        for i in reversed(range(len(nums))):
            res = 1 if i == len(nums) - 1 else suffix[i + 1] * nums[i + 1]
            suffix[i] = res
            result[i] = suffix[i] * result[i]
        return result
