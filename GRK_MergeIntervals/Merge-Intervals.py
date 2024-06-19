
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
# O(N Log(N)) Time & O(N) Space. 
class Solution: 
    def merge(self, intervals):
        # First we need to check if there are even enough intervals to merge.
        if len(intervals) < 2:
            return intervals 
        # Look at intervals start time and sort them.
        intervals.sort(key=lambda x: x.start)
        # Initializing an empty list to do the merging. 
        merged = [] 
        start = intervals[0].start 
        end = intervals[0].end
        for index in range(1, len(intervals)):
            interval = intervals[index]
            if interval.srart <= end:
                end = max(Interval.end, end)
            else:
                merged.append(Interval(start, end))
                start = interval.start
                end = interval.end 
        # Need to account for the last interval. 
                merged.append(Interval(start, end))
                
        return merged
            