class Solution: # O(N) Time & O(N) Space. 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = defaultdict(int)
        for character in magazine: 
            hashMap[character] += 1 
        for character in ransomNote:
            if hashMap[character] == 0: 
                return False 
            hashMap[character] -= 1
        return True  