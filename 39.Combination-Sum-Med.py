class Solution: # O(2^n) Time & O(N) Space. 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res 

    def dfs(self, candidates, start, target, comb, res):
        if target == 0: 
            res.append(list(comb))
            return 
        for index in range(start, len(candidates)):
            if target < candidates[index]:
                continue 
            comb.append(candidates[index])
            self.dfs(candidates, index, target - candidates[index], comb, res)
            comb.pop()