class Solution: # O(N)^2 Time and O(N) Space 
    def searchTriplets(self, arr, target):
        # constraints: triplets that have a sum less than targetr and three different indices 
        # Return the total count of these.
        # Sort the input array 
        arr.sort() 
        # Tracking the total count
        count = 0 
        # Iterate through the input array 
        for index in range(len(arr) - 2): 
            count += self.searchPairs(arr, target- arr[index], index + 1)
        return count 
    # Helper method to find corresponding pair 
    def searchPairs(self, arr, target_sum, left):
        # Track count in this method 
        count = 0 
        # Initialize a right pointer 
        right = len(arr) - 1 
        # Iterate through untile pointers are about to cross 
        while left < right: 
            # tracking current sum 
            curr_sum = arr[left] + arr[right]
            # Conditionals to check what to do with pointers 
            if curr_sum < target_sum: 
                count += right - left 
                left += 1 
            else: 
                right -= 1 
        return count 