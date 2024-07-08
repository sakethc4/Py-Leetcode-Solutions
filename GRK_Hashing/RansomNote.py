from collections import defaultdict
from collections import Counter
class Solution: # O(N) Time & O(1) Space. 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = defaultdict(int)
        for char in magazine: 
            hashMap[char] += 1
        # Now we can iterate thru ransomNote.
        for char in ransomNote: 
            if hashMap[char] == 0: 
                return False 
            hashMap[char] -= 1
        return True 
         