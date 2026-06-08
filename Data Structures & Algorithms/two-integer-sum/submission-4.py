class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {nums[0]: 0}
        list = []
        for x in range(1, len(nums)):
            if target - nums[x] in stored:
                list = [stored.get(target-nums[x]), x]
                return list
            else:
                stored[nums[x]] = x