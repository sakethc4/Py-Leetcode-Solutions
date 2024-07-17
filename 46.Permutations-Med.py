class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        self.backtrack(result, nums, [])
        return result 
    
    def backtrack(self, result, nums, currPerm):
        if len(currPerm) == len(nums):
            result.append(list(currPerm))
            return

        for index in range(len(nums)):
            if nums[index] in currPerm:
                continue 
            currPerm.append(nums[index])
            self.backtrack(result, nums, currPerm)
            currPerm.pop()