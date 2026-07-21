class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            i = (l + r) // 2
            res = min(res, nums[i], nums[r], nums[l])
            if nums[i] > nums[r]:
                l = i + 1
            else:
                r = i - 1
        return res
                
