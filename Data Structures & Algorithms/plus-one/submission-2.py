class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        add = False
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            add = True
        for i in range(len(digits) - 1, -1, -1):
            if add:
                if digits[i] != 9:
                    digits[i] += 1
                    add = False
                else:
                    digits[i] = 0
                    add = True
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits