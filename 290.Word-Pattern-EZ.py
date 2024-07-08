class Solution: # O(N) Time & O(1) Space. 
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {} 
        s2 = s.split()
        if len(pattern) != len(s2):
            return False 
        for (letter, word) in zip(pattern, s2):
            if letter in hashMap:
                if hashMap[letter] != word:
                    return False 
            elif word in hashMap.values():
                return False 
            else:
                hashMap[letter] = word 
        return True 