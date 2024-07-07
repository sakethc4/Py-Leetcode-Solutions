class Solution: # O(N) Time & O(N) Space. 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Track output.
        output = [] 
        q = collections.deque()
        start = end = 0 
        while end < len(nums):
            while q and nums[q[-1]] < nums[end]:
                q.pop() 
            q.append(end)
            # Shrinking window. 
            if start > q[0]:
                q.popleft()
            if (end + 1) >= k:
                output.append(nums[q[0]])
                start += 1 
            end += 1 
        return output
