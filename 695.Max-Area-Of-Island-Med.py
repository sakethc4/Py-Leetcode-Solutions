class Solution: # O(M * N) Time & O(M * N) Space. 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area  = 0 
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == 1:
                    area = max(area, self.dfs(grid, i, j))

        return area 

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0 
        if grid[row][col] == 0:
            return 0 

        grid[row][col] = 0 
        currArea = 1
        currArea += self.dfs(grid, row, col + 1)
        currArea += self.dfs(grid, row, col - 1)
        currArea += self.dfs(grid, row + 1, col)
        currArea += self.dfs(grid, row - 1, col)

        return currArea 
