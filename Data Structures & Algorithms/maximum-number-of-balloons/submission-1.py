class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        myDict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i == 'a' or i == 'b' or i == 'l' or i == 'o' or i == 'n':
                myDict[i] = myDict.get(i, 0) + 1
        myDict['l'] = myDict['l'] // 2
        myDict['o'] = myDict['o'] // 2
        return min(myDict.values())