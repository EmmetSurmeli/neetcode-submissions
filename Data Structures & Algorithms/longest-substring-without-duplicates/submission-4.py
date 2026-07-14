class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        left = 0
        myDict = {}
        for i in range(len(s)):
            if s[i] not in myDict:
                myDict[s[i]] = i
                current += 1
                longest = max(longest, current)
            else:
                longest = max(longest, current)
                left = max(left, myDict[s[i]] + 1)
                current = i - left + 1
                myDict[s[i]] = i
        return longest