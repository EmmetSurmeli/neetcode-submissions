class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums) 
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]
        myList = [0] * len(nums)
        for k in range(1, len(nums) - 1):
            myList[k] = prefix[k - 1] * suffix[k + 1]
        myList[0] = suffix[1]
        myList[-1] = prefix[-2]
        return myList