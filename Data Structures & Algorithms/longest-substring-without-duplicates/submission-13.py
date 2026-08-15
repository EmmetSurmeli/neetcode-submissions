class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        myDict = {}
        l = 0
        for i in range(len(s)):
            if s[i] in myDict:
                l = max(myDict[s[i]] + 1, l)
                curr = i - l + 1
            else:
                curr += 1
            myDict[s[i]] = i
            longest = max(longest, curr)
        return longest