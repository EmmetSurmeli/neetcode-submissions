class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set(nums)
        high = 0
        for i in mySet:
            if i - 1 not in mySet:
                length = 1
                while i + length in mySet:
                    length += 1
                high = max(high, length)
            

        return high