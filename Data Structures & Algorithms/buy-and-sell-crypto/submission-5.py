class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        low = prices[0]
        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - low)
            low = min(prices[i], low)
        return maxProf