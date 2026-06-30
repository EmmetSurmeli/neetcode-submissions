class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odds = set()
        for i in nums:
            if i in odds:
                odds.remove(i)
            else:
                odds.add(i)
        return not odds