class Solution:
    def isValid(self, s): # O(N) Time & O(N) Space. 
        # Want to check is parentheses input is valid. So opening and closing are both there. 
        map = {")" : "(", "]" : "[", "}" : "{"}
        # Let's also leverage a stack. 
        stack = [] 
        for character in s: 
            # Check to see if it's a valid character.
            if character not in map:
                stack.append(character)
                continue 
            if not stack or stack[-1] != map[character]:
                return False 
            stack.pop()
        # Return statement. 
        return not stack  
