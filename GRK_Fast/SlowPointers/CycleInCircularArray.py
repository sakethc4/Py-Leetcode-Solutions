class Solution: # O(N)^2 Time and O(1) Space 
    def loopExists(self, arr):
        # Input: [1, 2, -1, 2, 2]
        #         0 -> 1 -> 3 -> 0 
        # More than one element, and we have to be moving in the same direction. 
        # Observe if you take two pointers. Slow and the other one is fast. (slow can move 1) & (fast moves by 2). 
        # If slow == fast we have a cycle. 
        # Validate the input make sure array isn't null.
        if arr is None:
            return False 
        # Iterate through the input array. (For loop to track indices). 
        for index in range(len(arr)):
            isForward = arr[index] >= 0  
            # Initialize slow and fast pointers. 
            slow, fast = index, index 
            # Each iteration looking at a specific index.
            # Loop until we hit a break statement (while True:)
            while True:
                # Move slow by 1
                slow = self.findNextIndex(arr, isForward, slow) 
                fast = self.findNextIndex(arr, isForward, fast) 
                if (fast != -1):
                    # another call to fast.
                    fast = self.findNextIndex(arr, isForward, fast) 
                if slow == -1 or fast == -1 or slow == fast:
                    break 

            if slow != -1 and slow == fast: 
                    return True 
                
        return False 
            # I'll create a helper function to determine the next index we move to. 
    def findNextIndex(self, arr, isForward, index):
        currentDirection = arr[index] >= 0
        # We can look at currDirection = arr[index] >= 0 if != isForward return -1. 
        if currentDirection != isForward:
            return -1 
        # Calculating next index we want to move to. 
        nextIndex = (index + arr[index]) % len(arr)
        # One element cycle -> if nextIndex == currentIndex. --> return -1. 
        if nextIndex == index:
            return -1

        return nextIndex  
