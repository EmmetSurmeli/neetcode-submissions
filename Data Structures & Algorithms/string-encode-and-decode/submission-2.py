class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for x in strs:
            encoded_string += str(len(x)) + ")" + x
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            length_str = ""
            while s[i] != ")":
                length_str += s[i]
                i += 1
            length_int = int(length_str)
            i += 1
            decoded_strs.append(s[i : i + length_int])
            i = i + length_int

        return decoded_strs
