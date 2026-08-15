class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        myDict = {}
        l = 0
        for i in range(len(s)):
            if s[i] in myDict:
                l = max(myDict[s[i]] + 1, l)
            myDict[s[i]] = i
            longest = max(longest, i - l + 1)
        return longest