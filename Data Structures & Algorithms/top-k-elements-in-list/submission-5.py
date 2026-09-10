class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = [[] for _ in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for n, c in count.items():
            temp[c].append(n)
        result = []
        for i in reversed(range(len(temp))):
            for num in temp[i]:
                result.append(num)
                if k == len(result):
                    return result
        return result


