class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = [] 
        self.dfs(candidates, target, result, subset, 0)
        return result
# [1, 2, 1] => sort => [1,1,2]
    def dfs(self, candidates, target, result, subset, start):
        if target == 0: 
            result.append(list(subset))
            return 
        elif target < 0:
            return 
        else: 
            prev = -1 
            for index in range(start, len(candidates)):
                if candidates[index] == prev:
                    continue
                subset.append(candidates[index])
                self.dfs(candidates, target - candidates[index], result, subset, index + 1)
                subset.pop()
                prev = candidates[index]