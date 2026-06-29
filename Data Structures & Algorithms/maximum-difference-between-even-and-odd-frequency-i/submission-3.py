class Solution:
    def maxDifference(self, s: str) -> int:
        myDict = {}
        for i in s:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        maxOdd = 0
        minEven = len(s)
        for i in myDict.values():
            if i % 2 == 0:
                minEven = min(minEven, i)
            else:
                maxOdd = max(maxOdd, i)
        return maxOdd - minEven


            
    