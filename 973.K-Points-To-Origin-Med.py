class Solution: # O(N + k Log N) Time & O(N) Space. 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result, minHeap = [], []
        for x, y in points: 
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        # Heapify. 
        heapq.heapify(minHeap)
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            result.append((x, y))

        return result 