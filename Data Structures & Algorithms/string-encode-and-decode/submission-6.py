class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i)) + '#' + i
        return output
    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            length = 0
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            output.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return output
