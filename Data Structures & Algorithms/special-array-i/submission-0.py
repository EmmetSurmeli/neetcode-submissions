class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums) -1):
            if self.isOdd(nums[i]):
                if self.isOdd(nums[i - 1]) or self.isOdd(nums[i + 1]):
                    return False
            else:
                if not self.isOdd(nums[i - 1]) or not self.isOdd(nums[i + 1]):
                    return False
        return True
    def isOdd(self, num: int) -> bool:
        return num % 2 == 1