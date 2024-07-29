class Solution: # O(M * N) Time & O(M * N) Space. 
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)

        return islands
    
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 
        if grid[row][col] == "0":
            return 

        grid[row][col] = "0" 
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)

