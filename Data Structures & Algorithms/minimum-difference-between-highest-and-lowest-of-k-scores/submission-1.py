class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        low = float('inf')
        nums.sort()
        l, r = 0, k - 1
        while r < len(nums):
            diff = nums[r] - nums[l]
            low = min(low, diff)
            l += 1
            r += 1
        return low