class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        maxodd = 0
        mineven = float('inf')
        for i, j in count.items():
            if j % 2 == 0:
                mineven = min(mineven, j)
            else:
                maxodd = max(maxodd, j)
        return maxodd - mineven