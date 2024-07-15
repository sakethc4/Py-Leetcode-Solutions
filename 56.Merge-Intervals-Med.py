class Solution: # O(N) Time & O(N) Space. 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [intervals[0]] 
        if len(intervals) < 2: 
            return intervals 
        intervals.sort(key:lambda, x: x[0])
        for interval in intervals:
            if result[-1][1] > interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result