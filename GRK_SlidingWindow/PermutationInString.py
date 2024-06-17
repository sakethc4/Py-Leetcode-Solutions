class Solution: # O(N + M) Time & O(M) Space. N is the str1 & M is the pattern input. 
    def findPermutation(self, str1, pattern):
        # Frequency map to track letter occurences. 
        charFrequency = {} 
        # We need a variable to track the number of character matches between str1 and pattern inputs.
        matches = 0 
        # Pointer to track the beignning of the window. 
        windowStart = 0 
        # Iterate through the pattern input and add the letters to our map. 
        for character in pattern:
            # Check if it's already in the map.
            if character not in charFrequency: 
                charFrequency[character] = 0
            charFrequency[character] += 1 
        # Now we need to determine if patterns exist in our input string. 
        # So iterate through input string (handling expanding window). 
        for windowEnd in range(len(str1)):
            rightChar = str1[windowEnd]
            if rightChar in charFrequency:
                charFrequency[rightChar] -= 1
                # If we have reached the right number of elements increment matches. 
                if charFrequency[rightChar] == 0:
                    matches += 1 
            # If we have found a pattern. 
            if matches == len(charFrequency):
                return True
            # Handling window shrinking. 
            if windowEnd >= len(pattern) - 1:
                leftChar = str1[windowStart]
                windowStart += 1 
                if leftChar in charFrequency:
                    if charFrequency == 0:
                        matches -= 1
                    charFrequency[leftChar] += 1
        # Return statement. 
        return False 
