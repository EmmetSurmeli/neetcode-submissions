class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        high = 0
        l = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            if (i - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            high = max(high, i - l + 1)
        return high