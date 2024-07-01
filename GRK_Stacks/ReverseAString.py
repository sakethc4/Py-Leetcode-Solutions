class Solution: # O(N) Time & O(N) Space. 
    def reverseString(self, s):
        stack = list(s)
        output = "" 
        # Now iterate through the stack and add to our output string. 
        for character in range(len(s)):
            output += stack.pop() 
        return output 
