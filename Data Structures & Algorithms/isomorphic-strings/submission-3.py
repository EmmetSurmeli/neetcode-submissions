class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myDict1 = {}
        myDict2 = {}
        i = 0
        if len(s) != len(t):
            return False
        while i < len(s):
            if (s[i] in myDict1 and myDict1[s[i]] != t[i]) or (t[i] in myDict2 and myDict2[t[i]] != s[i]):
                    return False
            myDict2[t[i]] = s[i]
            myDict1[s[i]] = t[i]
            i += 1
        return True