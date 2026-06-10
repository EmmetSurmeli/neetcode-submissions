class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        currentLow = prices[0]
        for n in prices:
            if n < currentLow:
                currentLow = n
            if n - currentLow > currentMax:
                currentMax = n - currentLow
        return currentMax