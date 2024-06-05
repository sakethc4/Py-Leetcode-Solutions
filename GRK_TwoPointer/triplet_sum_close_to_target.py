import math
class Solution: # O(N)^2 time and O(N) space (cuz of sorting)
    def searchTriplet(self, arr, target_sum):
        # O(N log N) sorting input array 
        arr.sort()
        # Need to track smallest value (just putting an arbitrary value for now)
        smallest = math.inf
        # Iterating through the input array. I'm just skipping the last two elements because no need to check those.  
        for index in range(len(arr) - 2): 
            # Initializing a left and right pointer 
            left = index + 1 
            right = len(arr) - 1
            # Iterating throuh possible combos till left and right pointers are about to cross
            while left < right: 
                target_difference = target_sum - arr[index] - arr[left] - arr[right]
                # Case 1 we found the exact triplet to get the value 
                if target_difference == 0:
                    return target_sum 
                # Case 2 we have a "valid" triplet but need to handle for a smaller value 
                if abs(target_difference) < abs(smallest) or (abs(target_difference) == abs(smallest) and target_difference > smallest):
                    smallest = target_difference

                # Moving the pointers accordingly 
                if target_difference > 0:
                    left += 1 
                else:
                    right -= 1 

