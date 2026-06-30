from collections import Counter
class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) & 1 == 1:
            return False
        count = Counter(nums)
        for i in count.values():
            if i & 1 == 1:
                return False
        return True