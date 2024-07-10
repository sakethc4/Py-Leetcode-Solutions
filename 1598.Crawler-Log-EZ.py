class Solution: # O(N) Time & O(N) Space. 
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for index in range(len(logs)):
            if logs[index] == '../':
                if stack:
                    stack.pop()
            elif logs[index] == './':
                continue
            else:
                stack.append(logs[index])
        return len(stack) 