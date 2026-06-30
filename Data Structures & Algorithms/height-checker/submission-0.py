class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights[:]
        temp.sort()
        counter = 0
        for i in range(len(heights)):
            if temp[i] != heights[i]:
                counter += 1
        return counter