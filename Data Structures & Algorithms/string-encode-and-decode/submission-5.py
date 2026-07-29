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
            str_length = ''
            while s[i] != '#':
                str_length += s[i]
                i += 1
            int_length = int(str_length)
            output.append(s[i + 1: i + int_length + 1])
            i += int_length + 1
        return output
