class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        for i in t:
            arr[ord(i) - ord('a')] -= 1
        return [0] * 26 == arr