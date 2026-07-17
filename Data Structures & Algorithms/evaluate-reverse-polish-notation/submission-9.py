class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for i in tokens:
            if i not in '+-*/':
                operands.append(int(i))
            else:
                if i == '+':
                    operands.append(operands.pop() + operands.pop())
                elif i == '-':
                    right = operands.pop()
                    left = operands.pop()
                    operands.append(left - right)
                elif i == '*':
                    operands.append(operands.pop() * operands.pop())
                else:
                    right = operands.pop()
                    left = operands.pop()
                    operands.append(int(left / right))
        return operands[-1] if operands else -1