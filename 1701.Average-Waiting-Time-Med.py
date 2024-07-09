class Solution: # O(N) Time & O(1) Space. 
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Iterate through input tracking start times. 
        # [1,2] start = 1, 1 + 2 - 1 = 2
        # [2, 5] if start < arrival: start immediately. start = 3, 3 + 5 - 2 = 6
        # [4, 3] if start < arrival: start immediately. start = 8, 8 + 3 - 4 = 7
        result = 0 
        start = 0  
        for arrival, time in customers:
            if start < arrival:
                start = arrival
            duration = start + time - arrival
            start = start + time 
            result += duration 
        return result / len(customers)
        