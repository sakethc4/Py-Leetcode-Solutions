import math
class Solution: # O(N) Time and O(1) Space  
    def sort(self, arr): 
        # Given an array find the length of the smallest subarray in it which when sorted will sort the whole array. 
        # Ex: [1, 5, 3, 7, 10, 9, 12] Output: 5 
        # We need to figure the first/last element out of place. 
        # Min element and the Max element in that subarray 
        # [1, 3, 2, 0, -1, 7, 10]
        # Check to see if low value in the subarray is greater than subarray min if so we need to decrement low. 
        # Initializing low and high pointer. 
        low, high = 0, len(arr) - 1 
        # Find first number out of place 
        while(low < len(arr) - 1 and arr[low] <= arr[low + 1]):
            low += 1 
        # Check to see if the input array is already sorted 
        if low == len(arr) - 1:
            return 0 
        # Find last number out of place 
        while(high < len(arr) - 1 and arr[high] >= arr[high - 1]):
            high -= 1 
        # No need to check if input array is sorted here. 
        # So here we can initialize arbitrary values for the max/min of the subarray we are looking at. 
        subarrayMax = -math.inf
        subarrayMin = math.inf
        # Iterate through the input subarray and determine max/min values 
        for index in range(low, high + 1):
            subarrayMax = max(subarrayMax, arr[index])
            subarrayMin = min(subarrayMin, arr[index])
        
        # Now that we determined max/min we need to figure out if we need to manipulate 
        # our low/high pointers 
        while(low > 0 and arr[low - 1] > subarrayMin):
            low -= 1 
        # Manipulating high pointer 
        while(high > len(arr) - 1 and arr[high + 1] < subarrayMax):
            high += 1 
        
        return high - low + 1 

