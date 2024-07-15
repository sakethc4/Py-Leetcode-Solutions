class Solution: # O(N) Time & O(N) Space. 
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if nums is None:
            return result
        index = 0 
        while index < len(nums):
            start = nums[index]
            while index < len(nums) - 1 and nums[index] + 1 == nums[index + 1]:
                index += 1

            if start != nums[index]:
                result.append(str(start) + "->" + str(nums[index]))
            else:
                result.append(str(start))
            index += 1
        
        return result 