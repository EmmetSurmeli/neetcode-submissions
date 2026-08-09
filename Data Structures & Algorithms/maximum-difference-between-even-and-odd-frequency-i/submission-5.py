class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        maxodd = 0
        mineven = float('inf')
        for i in count.values():
            if i % 2 == 0:
                mineven = min(mineven, i)
            else:
                maxodd = max(maxodd, i)
        return maxodd - mineven