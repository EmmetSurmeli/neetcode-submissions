class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myList = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            myList[i] = pref
            pref *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            myList[i] *= post
            post *= nums[i]
        return myList