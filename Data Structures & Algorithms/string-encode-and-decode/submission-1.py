class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i)) + '#' + i
        return output
    def decode(self, s: str) -> List[str]:
        i = 0
        myList = []
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            leng_int = int(length)
            myList.append(s[i: i + leng_int])
            i += leng_int 
        return myList