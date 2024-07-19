class Solution: # O(2^N) Time & O(N) Space. 
    def partition(self, s: str) -> List[List[str]]:
        result, partition = [], []
        def dfs(i):
            if i >= len(s):
                result.append(list(partition))
                return 
            else:
                for j in range(i, len(s)):
                    if self.isPalindrome(s, i, j):
                        partition.append(s[i: j + 1])
                        dfs(j + 1)
                        partition.pop()
        dfs(0)
        return result
           
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False 
            i, j = i + 1, j - 1
        return True 