class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
            if myDict[i] > len(nums)//2:
                return i