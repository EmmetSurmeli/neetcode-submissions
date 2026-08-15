class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            high = max(high, area)
        return high