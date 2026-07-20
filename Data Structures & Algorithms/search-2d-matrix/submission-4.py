class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] >= target:
                break
            else:  
                top = mid + 1
        row = top + (bottom - top) // 2
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


