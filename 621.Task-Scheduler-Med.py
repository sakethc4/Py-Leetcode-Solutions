class Solution: # MaxHeap prob. we can do this O()
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Need total count of tasks. 
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0 
        queue = deque()
        while maxHeap or queue:
            time += 1  
            # Check to see if we have any elements to look at. 
            if not maxHeap:
                time = queue[0][1]
            else:
                 cnt = 1 + heapq.heappop(maxHeap)
                 if cnt: 
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])



        return time 