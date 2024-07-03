class Solution: # So I did this in O(N log(N)) Time & O(1) Space. This can for sure be done in O(N) time if I implement my own 
# sorting and do it in O(N) Time though. 
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4: 
            return 0 
        # Sort input nums. 
        nums.sort()
        case1 = abs(nums[3] - nums[-1])
        case2 = abs(nums[2] - nums[-2])
        case3 = abs(nums[1] - nums[-3])
        case4 = abs(nums[0] - nums[-4])
        return min(case1, case2, case3, case4)


        # [3,3,4,5]
        # Okay so in what combination can we delete elements from our sorted array. 
            # del 3 start and 0 from end. 
            # del 2 start and 1 from end. 
            # del 1 start and 2 from end. 
            # del 0 from start and 3 from end.  
