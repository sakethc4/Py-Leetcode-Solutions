class Solution: # O(N) Time & O(N) Space. 
    def dailyTemperatures(self, temperatures):
        stack, result = [], [0] * len(temperatures)
        for index in range(len(temperatures)):
            # Iterate through the stack. 
            while stack and temperatures[index] > temperatures[stack[-1]]:
                i = stack.pop() 
                result[i] = index - i 

            stack.append(index)
        return result
