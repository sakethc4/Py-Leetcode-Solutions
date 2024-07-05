class Solution: # O(N) Time & O(1) Space. 
    def kthFactor(self, n: int, k: int) -> int:
        factors = 0 
        for index in range(1, n + 1): 
            if n % index == 0: 
                factors += 1
            if factors == k: 
                return index
        return -1  