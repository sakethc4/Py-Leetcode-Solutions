class Solution: # OLogN*M Time & O(1) Space. 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom: 
            middle = top + (bottom - top) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else: 
                break

        if not (top <= bottom):
            return False
        row = top + (bottom - top) // 2 
        start, end = 0, cols - 1 
        while start <= end: 
            middle = start + (end - start) // 2
            if matrix[row][middle] > target: 
                end = middle - 1 
            elif matrix[row][middle] < target:
                start = middle + 1
            else: 
                return True 
        return False 