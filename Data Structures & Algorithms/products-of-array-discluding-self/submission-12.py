class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        #calculate the prefix
        for i in range(len(nums)):
            result.append(result[i - 1] * nums[i - 1] if i != 0 else 1)
        
        suffix = 1
        #calculate the suffix & result
        for i in reversed(range(len(nums))):
            suffix = suffix * (1 if i == len(nums) -1 else nums[i + 1])
            result[i] = result[i] * suffix

        return result 