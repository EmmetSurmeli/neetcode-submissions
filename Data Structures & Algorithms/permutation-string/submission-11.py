class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr = [0] * 26
        for i in s1:
            arr[ord(i) - ord('a')] += 1
        count = [0] * 26
        left = 0
        for i in range(len(s1)):
            count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if count == arr:
                return True
            count[ord(s2[left]) - ord('a')] -= 1
            left += 1
            count[ord(s2[i]) - ord('a')] += 1          
        return count == arr
