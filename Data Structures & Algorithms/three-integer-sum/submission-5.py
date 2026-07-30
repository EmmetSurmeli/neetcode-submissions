class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if nums[i] > 0: 
                break
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                summy = nums[i] + nums[l] + nums[r]

                if summy == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif summy > 0:
                    r -= 1
                else:
                    l += 1
        return output
                
