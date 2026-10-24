class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        high = 0
        for i in nums:
            if i - 1 not in mySet:
                count = 1
                while i + 1 in mySet:
                    count += 1
                    high = max(high, count)
                    i += 1
                high = max(high, count)
        return high