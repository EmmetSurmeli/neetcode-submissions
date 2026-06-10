class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightleft = {')' : '(', '}' : '{', ']' : '['}
        for n in s:
            if n in rightleft:
                if stack and stack[-1] == rightleft[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False