class Solution: # O(N) Time & O(1) Space. 
    def isPalindrome(self, s: str) -> bool:
        # If palindrome it should spell the same both ways. 
        # We can look at input by comparing the beginning character and 
        # the last character. To do this we can initialize two pointers.
        left, right = 0, len(s) - 1 
        # We need to move our pointers until right before the cross. 
        while left < right: 
            # Check to see if the left value is a valid character. 
            while left < right and not s[left].isalnum():
                left += 1
            # Repeat that for the right side.
            while left < right and not s[right].isalnum():
                right -= 1 
            # We need to check if the characters at both ends are equal.
            if s[left].lower() != s[right].lower():
                return False 
            # If we do have valid characters. We need to move our pointers.
            left += 1 
            right -= 1 
        # Return True. 
        return True 
