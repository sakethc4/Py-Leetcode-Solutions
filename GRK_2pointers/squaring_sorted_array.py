class Solution: # O(N) Space and O(N) Time 
    def makeSquares(self, arr): 
        # Length of the input array 
        n = len(arr) 
        # List to store squares of the input array 
        squares = [0 for x in range(n)]
        # Initializing a tracker for largest index 
        highestSquareIndex = n - 1 
        # left and right pointers to iterate through and square input array elements 
        left, right = 0, len(arr) - 1 
        # Iterate through the array until pointers meet each other in the middle 
        while left <= right: 
            # Squaring elements at both the pointers 
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]
            # Check to see if leftSquare is bigger than rightSquare
            if leftSquare > rightSquare: 
                squares[highestSquareIndex] = leftSquare
                left += 1 
            else:
                squares[highestSquareIndex] = rightSquare
                right -= 1
            highestSquareIndex -= 1
        return squares
