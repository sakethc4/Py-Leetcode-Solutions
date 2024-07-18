class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, column = len(board), len(board[0])
        pathing = set() 
        
        def dfs(r, c, i):
            if i == len(word):
                return True 
            if (r < 0 or c < 0 
                or r >= row or c >= column
                or word[i] != board[r][c]
                or (r, c)in pathing):
                return False 
            else: 
                pathing.add((r, c))
                result = (dfs(r + 1, c, i + 1) or 
                        dfs(r - 1, c, i + 1) or 
                        dfs(r, c + 1, i + 1) or 
                        dfs(r, c - 1, i + 1))
                pathing.remove((r, c))
                return result

        for r in range(row): 
            for c in range(column):
                if dfs(r, c, 0):
                    return True 
        return False 