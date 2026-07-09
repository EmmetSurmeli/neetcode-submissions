class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets for each row, column, and 3x3
        # Space complexity would be O(27N) = O(N)
        # check where each number lies (which row, column, box)
        # and see if that number is in any of those sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)] 
        boxes = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                box = (r // 3) * 3 + c // 3
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True