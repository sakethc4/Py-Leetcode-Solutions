class Solution: # O(N * M) Time & Space. 
    def orangesRotting(self, matrix: List[List[int]]) -> int:
        queue = deque()
        time, fresh = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    fresh += 1 
                if matrix[i][j] == 2: 
                    queue.append((i, j))

        while queue and fresh > 0: 
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions: 
                    row, col = dr + r, dc + c 
                    if (row in range(len(matrix)) and col in range(len(matrix[0])) and matrix[row][col] == 1):
                        matrix[row][col] = 2 
                        queue.append((row, col))
                        fresh -= 1 
        
            time += 1 
        
        return time if fresh == 0 else -1

