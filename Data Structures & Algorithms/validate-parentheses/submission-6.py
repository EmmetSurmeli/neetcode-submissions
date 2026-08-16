class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {']': '[', '}': '{', ')': '('}
        for i in s:
            if i in myDict:
                if not stack or stack[-1] != myDict[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0