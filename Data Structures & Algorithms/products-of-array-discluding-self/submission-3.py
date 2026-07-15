class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] + [nums[0]] + [1] * (n - 2)
        for i in range(2, n):
            output[i] = output[i - 1] * nums[i - 1] #stores prefixes
        suffix = nums[-1]
        for i in range(n - 2, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output