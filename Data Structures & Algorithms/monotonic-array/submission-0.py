class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 0
        if nums[0] < nums[1]:
            inc = 1
        elif nums[0] > nums[1]:
            inc = -1
        for i in range(1, len(nums)):
            if inc == 1:
                if nums[i] < nums[i - 1]:
                    return False
            elif inc == -1:
                if nums[i] > nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    inc = 1
                elif nums[i] < nums[i - 1]:
                    inc = -1
        return True