class Solution: # O(NLogN) Time & O(1) Space. 
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Input validation.
        if points is None:
            return 0 
        # Sort based on end time. 
        points.sort(key=lambda x: x[1])
        arrow = 0
        end = points[0][1] 
        for index in range(1, len(points)):
            if points[index][0] <= end:
                continue
            else: 
                arrow += 1
                end = points[index][1]
        arrow += 1  
        return arrow 