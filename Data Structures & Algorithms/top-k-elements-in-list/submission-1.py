class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = [[] for _ in range(len(nums) + 1)]
        count = {}
        result = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for n, c in count.items():
            temp[c].append(n)
        for i in reversed(range(len(temp))):
            for num in temp[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        
