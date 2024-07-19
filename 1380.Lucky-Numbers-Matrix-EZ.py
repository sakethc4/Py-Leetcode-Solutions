class Solution: # O(N) Time & O(N) Space. 
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Finding minimum in each row. 
        row_mins = [min(row) for row in matrix]  
        lucky_numbers = []
        
        for col in range(len(matrix[0])):  
            col_max = max(matrix[row][col] for row in range(len(matrix)))  
            if col_max in row_mins:
                lucky_numbers.append(col_max)
        
        return lucky_numbers