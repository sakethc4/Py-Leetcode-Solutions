class Solution: # O(N) Time & O(N) Space. 
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] 
        for character in s: 
            # Adding an occurence. 
            if stack and stack[-1][0] == character: 
                stack[-1][1] += 1
            # Adding to our stack.
            else: 
                stack.append([character, 1])
            # Removing from stack once we hit k. 
            if stack[-1][1] == k:
                stack.pop()

        return ''.join(character * number for character, number in stack)