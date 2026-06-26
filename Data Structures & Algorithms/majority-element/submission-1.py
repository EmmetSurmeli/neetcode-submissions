class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = 0
        c = 0
        for i in nums:
            if c == 0:
                r = i
            c += (1 if i == r else -1)
        return r
