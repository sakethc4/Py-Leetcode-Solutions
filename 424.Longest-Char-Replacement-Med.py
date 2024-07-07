class Solution: # O(N) Time & O(N) Space. 
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        charFrequency = {} 
        windowStart = 0
        repetitions = 0  
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar not in charFrequency: 
                charFrequency[rightChar] = 0 
            charFrequency[rightChar] += 1
            repetitions = max(repetitions, charFrequency[rightChar])
            # Now what happens if the window shrinks. 
            if (windowEnd - windowStart + 1 - repetitions) > k: 
                leftChar = s[windowStart]
                charFrequency[leftChar] -= 1 
                if charFrequency[leftChar] == 0:
                    del charFrequency[leftChar]
                windowStart += 1 
            longest = max(longest, windowEnd - windowStart + 1)
        return longest 

