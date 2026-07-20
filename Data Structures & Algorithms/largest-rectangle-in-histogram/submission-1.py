class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                width = i - stack[-1] - 1
                maxArea = max(maxArea, heights[index] * width)
            stack.append(i)
        while stack[-1] != -1:
            maxArea = max(maxArea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxArea