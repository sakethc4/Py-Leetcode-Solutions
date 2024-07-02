class Solution: # O(N)^2 Time * O(N) Space. 
    def sortStack(self,stack):
        tempStack = []
        while stack: 
            tempValue = stack.pop()
            while tempStack and tempStack[-1] > tempValue: 
                stack.append(tempStack.pop())
            tempStack.append(tempValue)
        return tempStack  
