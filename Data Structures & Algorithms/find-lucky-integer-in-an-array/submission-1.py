from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        high = -1
        for i in count:
            if count[i] == i:
                high = max(high, i)
        return high
        