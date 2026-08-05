class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        low = prices[0]
        for i in prices[1:]:
            if i < low:
                low = i
            else:
                high = max(high, i - low)
        return high