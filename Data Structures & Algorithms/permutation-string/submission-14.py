class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        sub = [0] * 26
        for i in s1:
            sub[ord(i) - ord('a')] += 1
        curr = [0] * 26
        for i in range(len(s1)):
            curr[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s1), len(s2)):
            if curr == sub:
                return True
            curr[ord(s2[i]) - ord('a')] += 1
            curr[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return curr == sub