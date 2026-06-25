class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myDict1 = {}
        myDict2 = {}
        i = 0
        if len(s) != len(t):
            return False
        while i < len(s):
            if s[i] not in myDict1:
                myDict1[s[i]] = t[i]
            else:
                if myDict1[s[i]] != t[i]:
                    return False
            if t[i] not in myDict2:
                myDict2[t[i]] = s[i]
            else:
                if myDict2[t[i]] != s[i]:
                    return False
            i += 1
        return True