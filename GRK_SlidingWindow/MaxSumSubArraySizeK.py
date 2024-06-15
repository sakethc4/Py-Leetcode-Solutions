class Solution: # Time O(N * K) & Space is O(1).
    def findMaxSumSubArray(self, k, arr): 
        # Given positive numbers and a postivie k. Find maximum sum of 
        # contiguous subarray or size k.
        # Validaitng our input  
        if arr is None or k is None or k <= 0:
            return -1 
        # Loop through the input. 
        # WindowSum to track the sum. 
        windowSum = 0
        result = 0 
        for i in range(len(arr) - k + 1):
            # Reset the sum for each new window. 
            windowSum = 0 
            for j in range(i, i + k):
            # Add the element to the windowSum.
                windowSum += arr[j]
            # Slide the window if necessary 
            result = max(windowSum, result)        
        return result 
                

        


