class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        output = [0] * len(nums)
        out_index = len(nums) - 1
        while out_index > 0:
            if abs(nums[l]) < abs(nums[r]):
                output[out_index] = nums[r] * nums[r]
                r -= 1
            elif abs(nums[l]) > abs(nums[r]):
                output[out_index] = nums[l] * nums[l]
                l += 1
            else:
                output[out_index] = nums[r] * nums[r]
                output[out_index - 1] = nums[r] * nums[r]
                out_index -= 1
                r -= 1
                l += 1
            out_index -= 1
        output[0] = nums[r] * nums[r]
        return output