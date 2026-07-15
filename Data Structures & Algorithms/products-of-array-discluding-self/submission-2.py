class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] + [0] * (len(nums) - 1)
        suffix = [0] * (len(nums) - 1) + [nums[-1]]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]
        output = [suffix[1]] + [1] * (len(nums) - 2) + [prefix[-2]]
        for i in range(1, len(nums) - 1):
            output[i] = prefix[i - 1] * suffix[i + 1]
        return output