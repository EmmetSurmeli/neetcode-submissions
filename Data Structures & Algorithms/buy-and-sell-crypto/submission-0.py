class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProf = 0
        smallest = prices[0]
        for i in prices:
            if i < smallest:
                smallest = i
            elif (i - smallest) > currentProf:
                currentProf = i - smallest
        return currentProf
