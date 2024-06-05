class Solution: # O(N)^2 Time and O(N) Space 
    def findSubarrays(self, arr, target): 
        # problem -> so we take in an input and 
        # provide all the contiguous subarrays where the product is less than the target. 
        # [2, 5, 3, 10] target = 30 
        # [2, 5, 3, 10] -> [2], [2,5] [5,3] shift our left pointer [10]
        # Unsure if sorting is needed by sorting input array 
        arr.sort()
        # Variable for output 
        results = [] 
        # Track the current product 
        product = 1.0 
        # Left boundary 
        left = 0 
        # Iterate through the input array 
        for right in range(len(arr)):
            # Figure out our product 
            product *= arr[right]
            # Now need to see if product is greater than or equal to our target 
            while product >= target and left < len(arr):
                product /= arr[left]
                left += 1 

            # Need to store the current subarray 
            temp_subarray = []

            # Iterate from right to left and add all the subarrays for output 
            for index in range(right, left - 1, -1): 
                temp_subarray.insert(0, arr[index])
                results.append(list(temp_subarray))
        
        return results 