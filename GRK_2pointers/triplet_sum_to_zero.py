class Solution: # O(N)^2 time and O(N) space 
    def searchTriplets(self, arr):
        # Array to hold output values
        triplets = [] # O(1) Space 
        # Sort the array so we can leverage a two pointer approach 
        arr.sort()  
        # Iterate through the input array 
        for index in range(len(arr)):
            # If we utilize helper on same arr element we get duplicate outputs so 
            # checking to ensure we aren't out of bounds and we are not passing in duplicates. 
            if index > 0 and arr[index - 1] == arr[index]:
                continue 
            else:
                # Make a call to our helper method to retrieve the corresponding pair 
                self.findpairs(arr, -arr[index], index + 1, triplets)
    
    def findPairs(self, arr, target_sum, left, triplets): 
        # Initialize a right pointer to find desired element 
        right = len(arr) - 1 
        # Iterate through until right before our pointers cross 
        while left < right: 
            curr_sum = arr[left] + arr[right]
            if curr_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1 
                right -= 1 
                while left < right and arr[left] == arr[left - 1]:
                    left += 1 
                while left < right and arr[right - 1]:
                    right -= 1 
            elif target_sum > curr_sum:
                left += 1 
            else: 
                right -= 1 
            

        