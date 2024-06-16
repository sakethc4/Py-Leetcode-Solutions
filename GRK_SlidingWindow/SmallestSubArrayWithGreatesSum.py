import math

class Solution: # O(N) Time & O(1) Space
  def findMinSubArray(self, s, arr):
    # Validate our input. 
    if s is None or arr is None:
      return 0 
    # minimumWindowLength
    minimumWindowLength = math.inf 
    # Track the current sum of the window we are looking at. 
    windowSum = 0 
    # Pointer where window begins. 
    windowStart = 0 
    # Iterate through out input array. 
    for windowEnd in range(0, len(arr)):
      # Adding the values to our windowSum 
      windowSum += arr[windowEnd]
      # Iterate through our window and shrink it up until we don't have sum >= s variable.
      while (windowSum >= s): 
        # We want to find the new smallest window. 
        minimumWindowLength = min(minimumWindowLength, windowEnd - windowStart + 1)
        # We want to remove the sum value associated with windowStart 
        windowSum -= arr[windowStart]
        # Move our windowStart pointer forward. 
        windowStart += 1 
    # Case where we go through and find no window gives us the desired value. 
    if minimumWindowLength == math.inf:
      return 0 
    # Return result 
    return minimumWindowLength
        

    
