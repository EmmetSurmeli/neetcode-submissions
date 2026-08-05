class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set(nums)
        highest = 0
        for i in mySet:
            if i - 1 not in mySet:
                length = 0
                while i + length in mySet:
                    length += 1
                highest = max(length, highest)
        return highest