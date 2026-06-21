class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        prefixes[0] = nums[0]

        suffixes = [0] * len(nums)
        suffixes[-1] = nums[-1]

        output = [0] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            suffixes[j] = suffixes[j + 1] * nums[j]
        for n in range(len(nums)):
            left = prefixes[n-1] if n > 0 else 1
            right = suffixes[n + 1] if n < len(nums) - 1 else 1
            output[n] = left * right

        return output