class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
                maxim = max(current, maxim)
            else:
                current = 0
        return maxim
