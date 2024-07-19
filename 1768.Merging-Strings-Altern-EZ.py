class Solution: # O(N) Time & O(N) Space. 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # "ab", "pqrs" => "apbqrs" 
        minLen = min(len(word1), len(word2))
        result = ""
        count = 0
        while count < minLen:
            result += word1[count]
            result += word2[count]
            count += 1 

        if len(word1) - count > 0:
            result += word1[count:]
        if len(word2) - count > 0:
            result += word2[count:]
        
        return result 