class Solution: # O(M * N) Time & Space. 
    def solve(self, board: List[List[str]]) -> None:
        # When we come across an O two outcomes => either we can flip it or it's not surrounded (remains as O). 
        rows, cols = len(board), len(board[0])
        # define a dfs function to move through the board. 
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O"): 
                return

            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Well now we need to mark unsurrounded. 
        for i in range(rows):
            for j in range(cols): 
                if board[i][j] == "O" and (i in [0, rows - 1] or j in [0, cols - 1]):
                    dfs(i, j)

        # Now mark regions with an x. 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Remark O's to replace T. 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"