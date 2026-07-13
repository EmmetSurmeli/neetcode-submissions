class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = prices[0]
        for i in prices:
            maxProf = max(i - buy, maxProf)
            buy = min(i, buy)
        return maxProf