class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            summy = numbers[l] + numbers[r]
            if summy == target:
                return [l + 1, r + 1]
            if summy > target:
                r -= 1
            else:
                l += 1