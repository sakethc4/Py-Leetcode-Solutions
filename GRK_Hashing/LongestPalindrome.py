class Solution: # O(N) Time & O(1) Space. 
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        # Count elements in s. 
        hashMap = Counter(s)
        
        length = 0
        oddFound = False
        
        for freq in hashMap.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                oddFound = True
        
        if oddFound:
            length += 1
        
        return length
