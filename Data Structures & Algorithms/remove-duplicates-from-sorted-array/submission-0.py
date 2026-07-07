class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums) 
        length = len(nums)
        i = 0
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                k -= 1
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return k