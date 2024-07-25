class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, temp = [], []
        def dfs(start): 
            if len(temp) == k:
                result.append(temp[:])
                return
 
            for index in range(start, n + 1):
                temp.append(index)
                dfs(index + 1)
                temp.pop()

        dfs(1)
        return result 


    # [1, 2] n => 1 k => 2 