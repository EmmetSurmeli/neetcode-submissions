class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ' and i > -1:
            counter += 1
            i -= 1
        return counter