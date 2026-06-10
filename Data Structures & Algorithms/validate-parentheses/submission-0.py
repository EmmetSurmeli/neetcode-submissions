class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in s:
            if n == '[' or n == '{' or n == '(':
                stack.append(n)
            else:
                if len(stack) == 0:
                    return False
                if n == ']':
                    if stack[-1] != '[':
                        return False
                elif n == '}':
                    if stack[-1] != '{':
                        return False
                else:
                    if stack[-1] != '(':
                        return False
                stack.pop()
        return True if len(stack) == 0 else False
                