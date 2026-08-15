class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]
                if value == '.':
                    continue
                if value in rows[row] or value in cols[col]:
                    return False
                if value in boxes[(row // 3) * 3 + col // 3]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boxes[(row // 3) * 3 + col // 3].add(value)
        return True