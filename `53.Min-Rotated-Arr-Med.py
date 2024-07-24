class Solution: # O(LogN) Time & O(1) Space. 
    def findMin(self, nums: List[int]) -> int:
        minimumVal = float("inf")
        start, end = 0, len(nums) - 1
        while start <= end: 
            middle = start + (end - start) // 2
            minimumVal = min(minimumVal, nums[middle])
            if nums[middle] > nums[end]:
                start = middle + 1 
            else: 
                end = middle - 1

        return minimumVal 
        # [3, 4, 5, 2, 1]
        # [1, 2, 3, 4, 5] 3 rotations. 