class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l = r
            else:
                return nums[r]
        return -1