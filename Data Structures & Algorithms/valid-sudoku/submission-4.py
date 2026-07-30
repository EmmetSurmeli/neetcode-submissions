class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        columns = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]
                if value == '.':
                    continue
                box = (r // 3) * 3 + c // 3
                if value in rows[r] or value in columns[c] or value in boxes[box]:
                    return False
                rows[r].add(value)
                columns[c].add(value)
                boxes[box].add(value)
        return True