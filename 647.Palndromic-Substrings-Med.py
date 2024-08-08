class Solution: # O(N^2) Time & O(1) Space. 
    def countSubstrings(self, s: str) -> int:
        # s = "abc" => "a", "b", "c". 
        count = 0 
        # Iterate through each epicenter. 
        for index in range(len(s)):
            # Handle odds.
            count += self.aux(s, index, index)
            # Handle evens.
            count += self.aux(s, index, index + 1)
        return count 

    
    def aux(self, s, left, right):
        count = 0 
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1 
            left -= 1 
            right += 1 
    
        return count 

