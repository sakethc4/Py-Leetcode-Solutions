class Solution: # O(N) Time & O(N) Space. 
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() 
        result = 0 
        length = 0 

        for index in range(len(s)):
            while s[index] in charSet: 
                charSet.remove(s[length])
                length += 1 
            charSet.add(s[index])
            result = max(result, index - length + 1)
        return result 