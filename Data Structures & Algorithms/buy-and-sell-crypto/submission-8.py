class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = 0
        for i in prices:
            high = max(high, i - low)
            low = min(low, i)
        return high