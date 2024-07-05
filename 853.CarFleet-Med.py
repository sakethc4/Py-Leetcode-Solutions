class Solution: # O(N) Time & O(N) Space. 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 

        for position, speed in sorted(zip(position, speed), reverse = True):
            timeOfArrival = (target - position) / speed 
            if not stack or timeOfArrival > stack[-1]:
                stack.append(timeOfArrival)
        return len(stack)
