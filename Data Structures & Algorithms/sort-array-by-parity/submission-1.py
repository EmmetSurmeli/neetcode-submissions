class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        arrIndex = 0
        out = [0] * len(nums)
        while arrIndex < len(nums):
            if nums[arrIndex] % 2 == 0:
                out[i] = nums[arrIndex]
                i += 1
            else:
                out[j] = nums[arrIndex]
                j -= 1
            arrIndex += 1   
        return out