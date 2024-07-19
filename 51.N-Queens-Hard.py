class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        posDiag = set() # row + col
        negDiag = set() # row - col

        result = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return 
            else:
                for c in range(n):
                    if c in columns or (r + c) in posDiag or (r - c) in negDiag:
                        continue
                    
                    columns.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    # backtrack. 
                    dfs(r + 1)
                    columns.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."

        dfs(0)
        return result
