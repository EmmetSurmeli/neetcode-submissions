class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = [set() for _ in range(len(board))]
        cset = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != '.':
                    if board[r][c] in rset[r] or board[r][c] in cset[c] or board[r][c] in boxes[(r // 3) * 3 + c // 3]:
                        return False
                    rset[r].add(board[r][c])
                    cset[c].add(board[r][c])
                    boxes[(r // 3) * 3 + c // 3].add(board[r][c])
        return True