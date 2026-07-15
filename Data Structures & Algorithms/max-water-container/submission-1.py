class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            maxArea = max(min(heights[l], heights[r]) * (r - l), maxArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea