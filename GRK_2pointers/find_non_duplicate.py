class Solution:
    def remove(self, arr): # O(1) Space and O(N) time 
        # Tracking index, so we know where to move the next non duplicate element 
        index = 0
        # Variable to track the next element that isn't a duplicate 
        next_non_duplicate = 1 
        # Loop to iterate through the array 
        while index < len(arr): 
            # Check to see if we have reached a new non duplicate element. 
            if arr[next_non_duplicate - 1] != arr[index]:
                # We can change the next non duplicate to current index 
                arr[next_non_duplicate] = arr[index]
                # Move the next non duplicate pointer 
                next_non_duplicate += 1
            index += 1 
        return next_non_duplicate 
