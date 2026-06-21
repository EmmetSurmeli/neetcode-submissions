class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force 2
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[0:i] = [x * nums[i] for x in output[0:i]]
            if i < len(nums) - 1:
                output[i + 1: len(nums)] = [x * nums[i] for x in output[i + 1: len(nums)]]
            i += 1
        return output