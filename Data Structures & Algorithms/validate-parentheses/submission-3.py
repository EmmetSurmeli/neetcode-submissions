class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {')':'(', 
        '}':'{',
        ']': '['}
        for i in s:
            if i in myDict:
                if stack and stack[-1] == myDict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack