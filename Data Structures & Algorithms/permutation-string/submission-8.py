class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr = [0] * 26
        for i in s1:
            arr[ord(i) - ord('a')] += 1
        
        l = -1
        r = len(s1)
        temp = [0] * 26
        for i in range(len(s1)):
            temp[ord(s2[i]) - ord('a')] += 1

        for r in range(len(s1), len(s2)):
            if temp == arr: 
                return True
            l += 1
            temp[ord(s2[l]) - ord('a')] -= 1
            temp[ord(s2[r]) - ord('a')] += 1
 
        return temp == arr