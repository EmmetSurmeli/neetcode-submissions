class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]
        suff = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= suff
            suff *= nums[i]
        return output