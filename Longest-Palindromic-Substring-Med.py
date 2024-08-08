class Solution: # O(N)^2 Time & O(1) Space. 
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0 
        # Iterate thru with each char as epicenter. 
        for index in range(len(s)):
            # Odd pals. 
            left = right = index 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength: 
                    result = s[left : right + 1]
                    resultLength = right - left + 1  
                left -= 1 
                right += 1
            # Even pals. 
            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left : right + 1]
                    resultLength = right - left + 1
                left -= 1 
                right += 1 
        
        return result 
            