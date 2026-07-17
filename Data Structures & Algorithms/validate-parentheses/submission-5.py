class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {'[' : ']', '(': ')', '{': '}'}
        for i in s:
            if i in myDict:
                stack.append(i)
            elif stack:
                if i != myDict[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0