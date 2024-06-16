class Solution: # O(N) Time & O(K) Space 
    def findLength(self, str1, k):
        # We need to figure out the maximum length of a substring with k distinct characters.
        maxLength = 0 
        # Validate our input. 
        if str1 is None and k is None:
            return maxLength
        # Pointer to track the start of our window 
        windowStart = 0 
        # We also need to track the frequency of characters in our input. 
        charFrequency = {} 
        # Iterate through our input string. 
        for windowEnd in range(len(str1)): 
            rightChar = str1[windowEnd]
            if rightChar not in charFrequency:
                charFrequency[rightChar] = 0
            # Adding an occurence to our map.  
            charFrequency[rightChar] += 1 
            # Handling shrinking our window 
            while len(charFrequency) > k:
                # We need to remove that chars occurence from our frequency map. 
                leftChar = str1[windowStart]
                charFrequency[leftChar] -= 1 
                # Delete the entry completely if we reach 0 total occurences. 
                if charFrequency[leftChar] == 0: 
                    del charFrequency[leftChar]
                # Move windowStart up by 1. 
                windowStart += 1 
            # We also need to find the new maxLength 
            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength 