class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_sell = prices[0]
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] > prev_sell:
                profit = profit + prices[i] - prev_sell
                prev_sell = prices[i]
                i = i + 1
                continue
            if i == len(prices) - 1:
                return profit
            if prices[i] < prices[i + 1]:
                prev_sell = prices[i + 1]
                profit += prev_sell - prices[i]
                i = i + 2
            else:
                i = i + 1
        return profit