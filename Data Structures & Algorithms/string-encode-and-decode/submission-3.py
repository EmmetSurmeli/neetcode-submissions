class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i)) + '#' + i
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        if len(s) == 0:
            return []
        i = 0
        while i < len(s):
            length = ''
            intleng = 0
            while s[i] != '#':
                length += s[i]
                i += 1
            intleng = int(length)
            output.append(s[i + 1: i + 1 + intleng])
            i += intleng + 1
        return output