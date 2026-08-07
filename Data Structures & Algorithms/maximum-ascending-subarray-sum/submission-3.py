class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        high = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = nums[i]
            else:
                curr += nums[i]
            high = max(high, curr)
        return high