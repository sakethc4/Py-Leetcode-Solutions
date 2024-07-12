class Solution: # O(N) Time & O(N) Space. 
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def removeStr(pair, score):
            nonlocal s
            result = 0
            stack = []

            for char in s:
                if char == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    result += score
                else:
                    stack.append(char)
            s = ''.join(stack) 
            return result 


        result = 0
        pair = "ab" if x > y else "ba"
        result += removeStr(pair, max(x, y))
        result += removeStr(pair[::-1], min(x, y))
        return result 