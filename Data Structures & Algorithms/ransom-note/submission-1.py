class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26
        for i in magazine:
            letters[ord(i) - ord('a')] += 1
        for j in ransomNote:
            if letters[ord(j) - ord('a')] == 0:
                return False
            letters[ord(j) - ord('a')] -= 1
        return True
        #Time: O(m + r)
        #SPace: O(1)