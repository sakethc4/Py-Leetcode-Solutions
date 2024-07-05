class Solution: # O(N) Time & O(N) Space. 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                elementTemp, elementIndex = stack.pop()
                results[elementIndex] = index - elementIndex
            stack.append([temperature, index])
        return results