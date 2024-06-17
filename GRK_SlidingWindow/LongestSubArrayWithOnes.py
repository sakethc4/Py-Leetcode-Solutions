import math 
class Solution: # O(N) Time & O(1) Space 
    def findLength(self, arr, k):
        # We are trying to find max length of 1's. 
        maxLength = 0
        # Validating input. 
        if arr is None or k is None:
            return maxLength 
        # Return statement. 
        # Pointer to track the beginning of the window.
        windowStart = 0 
        # We also want to track the frequency of 1's. 
        numberFrequency = 0
        for windowEnd in range(len(arr)):
            if arr[windowEnd] == 1:
                numberFrequency += 1 
            # Handle shrinking the window.
            if (windowEnd - windowStart + 1 - numberFrequency) > k:
                if arr[windowStart] == 1:
                    numberFrequency -= 1
                windowStart += 1
            # Calculate the new largest window. 
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength  