class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq = 0
        myDict = {}
        for i in range(len(s)):
            if s[i] in myDict:
                myDict[s[i]] += 1
            else:
                myDict[s[i]] = 1
            freq = max(freq, myDict[s[i]])
            while (i - left + 1) - freq > k:
                myDict[s[left]] -= 1
                left += 1
            longest = max(longest, i - left + 1)
        return longest