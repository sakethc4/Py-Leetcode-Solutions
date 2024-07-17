class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = [] 
        self.dfs(result, subset, nums, 0)
        return result 

    def dfs(self, result, subset, nums, index):
        if index >= len(nums):
            result.append(list(subset))
            return 
        subset.append(nums[index])
        self.dfs(result, subset, nums, index + 1)
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        subset.pop()
        self.dfs(result, subset, nums, index + 1)