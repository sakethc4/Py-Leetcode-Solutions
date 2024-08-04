class MedianFinder:
    # O(Log N) Time & O(N) Space. 
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else: 
            heapq.heappush(self.minHeap, num)
        # Redistributing our heaps. 
        if len(self.maxHeap) > len(self.minHeap) + 1: 
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2 + self.minHeap[0] / 2
        return -self.maxHeap[0]