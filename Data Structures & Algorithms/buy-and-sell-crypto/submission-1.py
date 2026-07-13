class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = prices[0]
        i = 1
        while i < len(prices):
            maxProf = max(prices[i] - buy, maxProf)
            buy = min(prices[i], buy)
            i += 1
        return maxProf