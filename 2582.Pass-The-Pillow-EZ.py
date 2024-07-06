class Solution: # O(1) Time & O(1) Space. 
    def passThePillow(self, n: int, time: int) -> int:
        if time < n: 
            return time + 1 
        else: 
            timeNeeded = n - 1 # 1 
            cycles = time // timeNeeded # 1
            timeUsed = timeNeeded * cycles # 5 
            timeLeft = time - timeUsed # 0 
        if cycles % 2 == 0:
            return 1 + timeLeft
        else: 
            return n - timeLeft  
