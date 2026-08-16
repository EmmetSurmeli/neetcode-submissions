class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+*-/':
                stack.append(int(i))
            else:
                if i == '+':
                    val = stack.pop() + stack.pop()
                    stack.append(val)
                elif i == '-':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left - right)
                elif i == '*':
                    val = stack.pop() * stack.pop()
                    stack.append(val)
                else:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left / right))
        return stack[-1]