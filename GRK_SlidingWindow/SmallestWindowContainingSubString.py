class Solution: # O(N + M) & Time O(M) Space where N is str1 & M is the pattern input. 
    def findSubstring(self, str1, pattern):
        # Finding smallest substring. 
        result = len(str1) + 1 
        # Determine components in the pattern.
        # Initialize a frequency map.
        charFrequency = {} 
        # Pointer to track window start,
        windowStart = 0
        # Want to track number of fonud elements.
        matches = 0  
        # Iterate through our pattern and all elements to our map.
        for character in pattern:
            if character not in charFrequency:
                charFrequency[character] = 0 
            # Add an occurence.
            charFrequency[character] += 1
        # Iterate through our input string. Handle expanding our window.  
        for windowEnd in range(len(str1)):
            rightChar = str1[windowEnd]
            if rightChar in charFrequency:
                charFrequency[rightChar] -= 1
                if charFrequency[rightChar] >= 0:
                  matches += 1
            # Handling shrinking our window. 
            while matches == len(pattern):
                if result > windowEnd - windowStart + 1:
                    result = windowEnd - windowStart + 1 
                    startingIndex = windowStart 
                # Handling moving the windowStart pointer. 
                leftChar = str1[windowStart]
                windowStart += 1 
                if leftChar in charFrequency:
                    if charFrequency[leftChar] == 0:
                        matches -= 1 
                    charFrequency[leftChar] += 1
        # Check to see if we could not find the desired element. 
        if result > len(str1):
            return "" 
        # Return statement. 
        return str1[startingIndex: startingIndex + result] 