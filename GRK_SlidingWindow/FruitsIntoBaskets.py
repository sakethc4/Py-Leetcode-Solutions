class Solution: # O(N) Time and O(K) Space 
    def findLength(self, fruits): 
        # We want to find the max number of fruits we can get. 
        maxLength = 0 
        # pointer to track the beginning of our window.
        windowStart = 0 
        # We also need to keep track of the fruits we come across. 
        fruitFrequency = {} 
        # Iterate through the input array. 
        for windowEnd in range(len(fruits)):
            # Need to handle keeping track of new fruits. 
            rightFruit = fruits[windowEnd]
            # Checking to see if we already have that fruit. 
            if rightFruit not in fruitFrequency:
                fruitFrequency[rightFruit] = 0 
            # Otherwise add an occurence.
            fruitFrequency[rightFruit] += 1
            # Now we need to handle what happens when we shrink the window. 
            # If we have two fruit types we need to shrink. 
            while len(fruitFrequency) > 2:
                # When we do shrink we need to A) remove occurence of fruit B) remove fruit from map completely if necessary.
                leftFruit = fruits[windowStart]
                fruitFrequency[leftFruit] -= 1 
                if fruitFrequency[leftFruit] == 0:
                    del fruitFrequency[leftFruit]
                # Move our window start (after we shrink window). 
                windowStart += 1 
            # Determine a new max length. 
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        # Return statement. 
        return maxLength  