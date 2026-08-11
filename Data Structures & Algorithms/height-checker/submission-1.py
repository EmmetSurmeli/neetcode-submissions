class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorty = list(heights)
        sorty.sort()
        total = 0
        for i in range(len(sorty)):
            if heights[i] != sorty[i]:
                total += 1
        return total
        