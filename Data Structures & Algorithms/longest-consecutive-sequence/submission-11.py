class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums) # O(1) lookup
        high = 0
        for i in mySet:
            if i - 1 in mySet:
                continue
            curr = 1
            while i + 1 in mySet:
                curr += 1
                i += 1
            high = max(high, curr)
        return high