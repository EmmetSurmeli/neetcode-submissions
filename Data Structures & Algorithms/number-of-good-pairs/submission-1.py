class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        myDict = {}
        for i in nums:
            myDict[i] = myDict.get(i, 0) + 1
        counter = 0
        for n in myDict.values():
            counter += ((n - 1) * n) / 2
        return int(counter)