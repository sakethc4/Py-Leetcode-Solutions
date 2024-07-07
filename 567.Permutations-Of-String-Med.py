class Solution: # O(N) Time & O(N) Space. 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We need to know all the element in s1.
        hashMap = {}
        windowStart = 0  
        matches = 0 
        # Track values in s1. 
        for char in (s1):
            if char not in hashMap:
                hashMap[char] = 0 
            hashMap[char] += 1 
        # We need to iterate through and compare against s1.
        for windowEnd in range(len(s2)):
            rightChar = s2[windowEnd]
            if rightChar in hashMap: 
                hashMap[rightChar] -= 1 
                if hashMap[rightChar] == 0: 
                    matches += 1 
            # Check to see if we have correct number of matches.   
            if matches == len(hashMap):
                return True  
            # Handle shrinking the window. 
            if windowEnd >= len(s1) - 1:
                leftChar = s2[windowStart]
                windowStart += 1 
                if leftChar in hashMap: 
                    if hashMap[leftChar] == 0:
                        matches -= 1
                    hashMap[leftChar] += 1 
        return False 
