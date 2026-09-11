class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i == len(nums) -1:
                return result
            s = i + 1
            e = len(nums) -1
            while s < e:
                start = nums[s]
                end = nums[e]
                if nums[i] + start + end == 0:
                    if [nums[i], start, end] not in result:
                        result.append([nums[i], start, end])
                    s += 1
                elif nums[i] + start + end > 0:
                    e -= 1
                else:
                    s += 1
        return result
    