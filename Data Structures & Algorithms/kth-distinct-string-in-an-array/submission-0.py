from collections import Counter
class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct = 0
        for i in count:
            if count[i] == 1:
                distinct += 1
                if distinct == k:
                    return i
        return ''