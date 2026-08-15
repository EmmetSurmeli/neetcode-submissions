class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        for i in range(1, len(nums)):
            arr[i] *= nums[i - 1] * arr[i - 1]
        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            arr[i] *= curr
            curr *= nums[i]
        return arr