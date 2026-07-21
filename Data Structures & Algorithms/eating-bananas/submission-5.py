class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            hour = 0
            k = (l + r) // 2
            for i in piles:
                hour += math.ceil(i / k)
            if hour <= h:
                result = min(k, result)
                r = k - 1
            else:
                l  = k + 1
        return result
        