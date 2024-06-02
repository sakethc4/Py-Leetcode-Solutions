class Solution: # O(N) Time and O(1) Space 
    def sort(self, arr): 
        # Need to inplace sorting given an array of 0's, 1's, and 2's
        # Initialize a left and right pointer (left to keep track of where 0's should go) and right for the 2's 
        left, right = 0, len(arr) - 1 
        # Index to iterate through the input array 
        index = 0
        # Iterating through the input array 
        while(index <= right):
            # Case where the current index we are at is a one  
            if arr[index] == 1:
                index += 1 
            # Case where input is a zero 
            elif arr[index] == 0: 
                arr[index], arr[left] = arr[left], arr[index]
                left += 1
                index += 1  
                # Case for a two. 
            else: 
                arr[index], arr[right] = arr[right], arr[index]
                right -= 1 
        # Results 
        return arr                                  
