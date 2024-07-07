class Solution: # O(1) Time & Space. 
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
        