class Solution: # O(2^N) Time & O(N) Space. 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []
        self.dfs(res, nums, subset, 0)
        return res 

    def dfs(self, res, nums, subset, start):
        if start >= len(nums):
            res.append(list(subset))
            return 
        subset.append(nums[start])
        self.dfs(res, nums, subset, start + 1)
        subset.pop()
        self.dfs(res, nums, subset, start + 1)