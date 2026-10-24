class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"]":"[", ")":"(", "}":"{"}
        for i in s:
            if i in dictionary:
                if not stack or stack[-1] != dictionary[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack