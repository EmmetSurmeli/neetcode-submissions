class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict = {}
        for i in s:
            if i in myDict:
                myDict[i] = myDict[i] + 1
            else:
                myDict[i] = 1
        
        for j in t:
            if j not in myDict:
                return False
            else:
                myDict[j] = myDict[j] - 1
                if myDict[j] == 0:
                    myDict.pop(j)
        return False if myDict else True