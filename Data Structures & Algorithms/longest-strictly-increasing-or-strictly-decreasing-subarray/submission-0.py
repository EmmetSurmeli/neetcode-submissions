class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 0
        curr = nums[0]
        longest = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                temp = 1
                inc = 0
            elif nums[i] > nums[i - 1]:
                if inc > 0:
                    temp += 1
                else:
                    temp = 2
                    inc = 1
            else:
                if inc < 0:
                    temp += 1
                else:
                    temp = 2
                    inc = -1
            longest = max(longest, temp)
        return longest