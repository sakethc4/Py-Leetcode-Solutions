class Solution: # O(N) Time & O(N) Space. 
    def removeDuplicates(self, s: str) -> str:
        stack = [] 
        # Iterate through the input. 
        for char in s: 
            if stack and stack[-1] == char: 
                stack.pop() 
            else: 
                stack.append(char) 

        return ''.join(stack)