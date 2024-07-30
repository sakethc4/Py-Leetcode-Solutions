class Solution: # O(N) Time & O(1) Space. 
    def minimumDeletions(self, s: str) -> int:
        countB = 0
        result = 0
        for char in s: 
            if char == "a":
                result = min(result + 1, countB)
            else:
                countB += 1
        return result 