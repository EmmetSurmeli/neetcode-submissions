class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        buy = prices[0]
        for j in prices:
            maxprof = max(maxprof, j - buy)
            buy = min(buy, j)
        return maxprof