class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = []
        current = 0
        for i in nums:
            current += i
            self.pref.append(current)
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.pref[right]
        leftSum = self.pref[left - 1] if left != 0 else 0
        return rightSum - leftSum
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)