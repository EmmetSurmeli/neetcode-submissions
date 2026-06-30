class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        myDict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i == 'a' or i == 'b' or i == 'l' or i == 'o' or i == 'n':
                myDict[i] = myDict.get(i, 0) + 1
        counter = 0
        while myDict['b'] > 0 and myDict['a'] > 0 and myDict['l'] > 1 and myDict['o'] > 1 and myDict['n'] > 0:
            counter += 1
            myDict['b'] -= 1
            myDict['a'] -= 1
            myDict['l'] -= 2
            myDict['o'] -= 2
            myDict['n'] -= 1
        return counter