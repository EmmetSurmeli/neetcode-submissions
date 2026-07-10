class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for i in tokens:
            if i in '+-/*':
                operator = i
                if operator == '+':
                    operands.append(operands.pop() + operands.pop())
                elif operator == '-':
                    operands.append(-1 * operands.pop() + operands.pop())
                elif operator == '*':
                    operands.append(operands.pop() * operands.pop())
                else:
                    right = operands.pop()
                    left = operands.pop()
                    operands.append(int(left / right))
            else:
                operands.append(int(i))
        return int(operands[0])