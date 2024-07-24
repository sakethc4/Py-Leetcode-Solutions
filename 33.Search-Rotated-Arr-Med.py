class Solution: # O(LogN) Time & O(1) Space. 
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end: 
            middle = start + (end - start) // 2
            if nums[middle] == target: 
                return middle

            if nums[middle] >= nums[start]:
                if target > nums[middle] or nums[start] > target: 
                    start = middle + 1
                else: 
                    end = middle - 1 
            else: 
                if nums[end] < target or target < nums[middle]: 
                    end = middle - 1
                else: 
                    start = middle + 1
        return -1 


            # [1,2,0] Looking for 0. 

            # [4, 5, 6, 7, 0, 1, 2] target = 0. 