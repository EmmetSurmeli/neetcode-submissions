class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        inRow = False
        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                inRow = True
                break
            if matrix[row][0] > target:
                bottom = row - 1
            else:
                top = row + 1
        if inRow == False:
            return False

        # row is our row of interest
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False