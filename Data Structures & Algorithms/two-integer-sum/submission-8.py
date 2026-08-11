class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in myDict:
                return [myDict[target - nums[i]], i]
            myDict[nums[i]] = i