class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        current = 1
        for i in range(1, len(nums)):
            current *= nums[i - 1]
            output[i] *= current
        current = 1
        for i in range(len(nums) - 2, -1, -1):
            current *= nums[i + 1]
            output[i] *= current
        return output