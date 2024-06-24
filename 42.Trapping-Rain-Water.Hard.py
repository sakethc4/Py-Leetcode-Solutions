class Solution: # O(N) Time & O(1) Space.
    def trap(self, height: List[int]) -> int:
        # Validate input. 
        if height is None:
            return 0 
        # We want to return units of rain water. 
        water = 0 
        # Initialize two pointers to traverse input. 
        left, right = 0, len(height) - 1 
        # Finding max values for left, right. 
        maxLeft, maxRight = height[left], height[right]
        # Iterate through the input. 
        while left < right: 
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left] 
            else: 
                right -= 1 
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right] 
        # Return statement. 
        return water 


# Approach: 

# A location has rain water if it's enclosed by a block and the amount of rain 
# water is determined by min(l, r) boundaries. 

# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3] max left value
# [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0] max right value 
# [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0] min(l, r)                