class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        prefix_value = 1
        suffix_value = 1

        # calculate the prefix
        for i in range(len(nums)):
            prefix_value = 1 if i == 0 else prefix_value * nums[i-1]
            result.append(prefix_value)
        # calculate the suffix
        for i in reversed(range(len(nums))):
            suffix_value = 1 if i == len(nums) - 1 else suffix_value * nums[i+1]
            result[i] = result[i] * suffix_value

        return result