class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for j in range(len(nums)):
            rightSum -= nums[j]
            if leftSum == rightSum:
                return j
            leftSum += nums[j]
        return -1