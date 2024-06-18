class Solution: # O(N + M) Time & O(M) Space where N is str1 & M is the pattern. 
    def findStringAnagrams(self, str1, pattern):
        # We want to return starting indices of pattern permutations.
        results = []
        # Initialize a frequency map.
        charFrequency = {}
        # Pointer to track the beginning of the window.
        windowStart = 0
        # Variable to track the number of correct characters we have found.
        matches = 0 
        # Iterate through our input pattern and add components to map.
        for character in pattern:
            if character not in charFrequency:
                charFrequency[character] = 0
            # Add an occurence.
            charFrequency[character] += 1 
        # Expanding our window. 
        for windowEnd in range(len(str1)):
            rightChar = str1[windowEnd]
            if rightChar in charFrequency:
                charFrequency[rightChar] -= 1
                if charFrequency[rightChar] == 0:
                    matches += 1
            # If we have reached partity add the starting index to results. 
            if matches == len(charFrequency):
              results.append(windowStart)
            # Handling shrinking the window. 
            if windowEnd - windowStart + 1 >= len(pattern):
                leftChar = str1[windowStart]
                windowStart += 1
                if leftChar in charFrequency:
                    if charFrequency[leftChar] == 0:
                        matches -= 1
                    # We want to increment by 1.
                    charFrequency[leftChar] += 1 
        # Return statement.
        return results