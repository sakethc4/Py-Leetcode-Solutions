class Solution: # O(N)^2 Time & O(N) Space. 
    # Trying to check if row moves 1-9 (no duplicates)
    # Checking to make sure each column contains the digits 1-9. 
    # Each of the nine 3 x 3 sub-boxes of the grid must contain digits 1-9
    # (no duplicates).            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Declaring a default dict hashSet to store our column vals. 
        # O(n) space complex. 
        # Track elements in each row.
        rows = collections.defaultdict(set)
        # Track in each column.
        cols = collections.defaultdict(set)
        # Track in each sub box. 
        box = collections.defaultdict(set)
        # We want to iterate through the rows. 
        for row in range(9):
            for column in range(9):
                # Check if empty or filled square.
                if board[row][column] == ".":
                    continue
                # Check to see if we have encountered the value. 
                if (board[row][column] in rows[row]  
                    or board[row][column] in cols[column]  
                    or board[row][column] in box[row // 3, column // 3]):
                        return False 
                # Otherwise add to our set. 
                cols[column].add(board[row][column])
                rows[row].add(board[row][column])
                box[row // 3, column // 3].add(board[row][column])
        return True 

        