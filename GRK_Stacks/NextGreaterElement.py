class Solution: # O(N) Time & O(N) Space. 
    def nextLargerElement(self, arr):
        result = [-1] * len(arr)
        stack = [] 
        # Iterate through our input. 
        for index in range(len(arr) - 1, -1, -1): 
            while stack and stack[-1] <= arr[index]: 
                stack.pop() 
            if stack:
                result[index] = stack[-1]
            # Append the elements we are looking at. 
            stack.append(arr[index])
        
        return result 
