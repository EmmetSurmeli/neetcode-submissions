class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = {}
        longest = 0
        current = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in myDict:
                current += 1
            else:
                longest = max(longest, current)
                left = max(myDict[s[i]] + 1, left)
                current = i - left + 1
            myDict[s[i]]= i    
        longest = max(longest, current)
        return longest