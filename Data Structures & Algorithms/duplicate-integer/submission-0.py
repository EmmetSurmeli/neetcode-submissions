class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored = set()
        for x in nums:
            if x in stored:
                return True
            else:
                stored.add(x)
        return False