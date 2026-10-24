class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        i = 0
        nums = sorted(nums)
        while i < len(nums) and nums[i] <= 0:
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1 
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return output