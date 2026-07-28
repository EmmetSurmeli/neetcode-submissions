class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
