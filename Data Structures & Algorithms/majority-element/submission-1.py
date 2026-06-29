class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        number = nums[0]
        for i in nums:
            if i == number:
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                counter = 1
                number = i
        return number