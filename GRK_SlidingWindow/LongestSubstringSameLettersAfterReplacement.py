class Solution: # O(N) Time and O(1) Space. 
    def findLength(self, str1, k):
        # We are trying to find the max length of substring with k replacements.
        maxLength = 0 
        # Validating the input. 
        if str1 is None and k is None:
            return maxLength 
        # We need to track how many time we made rpelacements.
        maxRepeatLetter = 0
        # Frequency map to track occurences of letters. 
        charFrequency = {} 
        # Pointer to track where the window starts. 
        windowStart = 0 
        # Iterate through our input string. 
        for windowEnd in range(len(str1)):
            rightChar = str1[windowEnd]
            if rightChar not in charFrequency:
                charFrequency[rightChar] = 0 
            # Otherwise add an occurence.
            charFrequency[rightChar] += 1 
            # Replacing characters. 
            maxRepeatLetter = max(maxRepeatLetter, charFrequency[rightChar])
            # We need to handle shrinking the window. 
            if (windowEnd - windowStart + 1 - maxRepeatLetter) > k: 
                leftChar = str1[windowStart]
                charFrequency[leftChar] -= 1
                if charFrequency[leftChar] == 0:
                    del charFrequency[leftChar]
                # Move our windowStart pointer.
                windowStart += 1 
            # We need to get the new maximum window. 
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        # Return statement.
        return maxLength
