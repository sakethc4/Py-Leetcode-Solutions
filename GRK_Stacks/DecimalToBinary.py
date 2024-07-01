class Solution: # O(NLog(N)) Time & Space. 
    def decimalToBinary(self, num):
        stack = [] 
        while num > 0: 
            stack.append(num % 2)
            num //= 2 
        return ''.join(str(i) for i in reversed(stack))
