class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0

        for i in prices:
            profit = max(i - prev, profit)
            prev = min(i, prev)
        return profit