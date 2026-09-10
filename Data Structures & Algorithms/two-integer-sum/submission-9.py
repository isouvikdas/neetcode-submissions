class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            com = target - num
            if com in dic:
                return [dic[com], i]
            
            dic[num] = i
        return [-1, -1]