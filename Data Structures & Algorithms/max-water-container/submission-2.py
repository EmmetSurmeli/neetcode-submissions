class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        l = 0
        r = len(heights) - 1
        curr = 0
        while l < r:
            high = max(high, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            

        return high