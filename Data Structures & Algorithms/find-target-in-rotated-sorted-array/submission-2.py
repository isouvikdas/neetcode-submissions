class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r 
            if nums[l] <= nums[i]:
                if nums[l] <= target and target <= nums[i]:
                    r = i - 1
                else:
                    l = i + 1
            else:
                if nums[i] <= target and target <= nums[r]:
                    l = i + 1
                else:
                    r = i - 1
            
        return -1