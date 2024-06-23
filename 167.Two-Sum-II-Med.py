class Solution: # O(N) Time & O(1) Space. 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize a left bound and right bound. 
        left, right = 0, len(numbers) - 1
        # Iterate through our input. 
        while left < right: 
            # Track the current sum we have. 
            currentSum = numbers[left] + numbers[right]
            # We need to determine how to manipulate our bounds. 
            if currentSum < target: 
                left += 1 
            elif currentSum > target: 
                right -= 1 
            # Otherwise we have found our sum. 
            else: 
                return[left + 1, right + 1]