class Solution: # O(N) Time & O(1) Space. 
    def maxArea(self, height: List[int]) -> int:
        # Need to track width from first data point 
        # No sorting needed.
        # We want to return maxArea.
        maxArea = 0 
        # Initialize pointers to track left and right bounds. 
        left, right = 0, len(height) - 1
        # Iterate through our input array. 
        while left < right: 
            width = right - left 
            # Now we need to determine the current maxArea. 
            maxArea = max(maxArea, min(height[right], height[left]) * width)
            # Now that we have that let's manipulate bounds. 
            if height[left] < height[right]:
                left += 1 
            # Otherwise move right bound. 
            else: 
                right -= 1 
        # Return here. 
        return maxArea 

        

