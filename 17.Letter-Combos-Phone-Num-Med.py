class Solution: # O(4^N) Time & O(N) Space. 
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
            }
        result = []
        def dfs(i, temp): 
            if len(temp) == len(digits):
                result.append(temp)
                return 
            else: 
                for char in letters[digits[i]]:
                    dfs(i + 1, temp + char)
        
        if digits: 
            dfs(0, "")
        return result

        
        
        # [2]
        # ["a", "b", "c"]
        #  