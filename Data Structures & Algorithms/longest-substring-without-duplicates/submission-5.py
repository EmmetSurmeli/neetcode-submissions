class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        myDict = {}
        for i in range(len(s)):
            if s[i] in myDict:
                left = max(myDict[s[i]] + 1, left)
            myDict[s[i]] = i
            longest = max(longest, i - left + 1)
        return longest