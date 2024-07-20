class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                value = min(rowSum[i], colSum[j])
                result[i][j] = value 

                rowSum[i] -= value
                colSum[j] -= value 

        return result