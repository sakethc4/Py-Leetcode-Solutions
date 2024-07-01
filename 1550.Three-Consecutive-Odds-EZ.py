class Solution: # O(N) Time & O(1) Space. 
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Iterate through input list, and track number of odds. 
        counter = 0 
        for number in arr: 
            # If it's even reset counter and skip that iteration. 
            if number % 2 == 0: 
                counter = 0
                continue 
            else: 
                counter += 1 
            if counter == 3: 
                return True 
        return False 