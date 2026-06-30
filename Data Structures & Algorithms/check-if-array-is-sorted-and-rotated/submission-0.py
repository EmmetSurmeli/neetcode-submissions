class Solution:
    def check(self, nums: List[int]) -> bool:
        index, mini = 0, nums[0]
        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
                index = i
        for j in range(index + 1, len(nums)):
            if nums[j] < nums[j - 1]:
                return False
        for k in range(index):
            if nums[0] < nums[-1]:
                return False
            if nums[k] < nums[k - 1]:
                return False
        return True